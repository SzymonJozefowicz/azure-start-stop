from msrestazure.azure_active_directory import MSIAuthentication
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient

# Create MSI Authentication
credentials = MSIAuthentication()


# Create a Subscription Client
subscription_client = SubscriptionClient(credentials)
subscription = next(subscription_client.subscriptions.list())
print(subscription)

subscription_id = subscription.subscription_id

subscription_name=""
i=0

for subscriptions in subscription_client.subscriptions.list():
    print(subscriptions.display_name)

    subscription_name=subscriptions.display_name
    subscription_id = subscriptions.subscription_id

# Create a Resource Management client
    resource_client = ResourceManagementClient(credentials, subscription_id)
    
# List resource groups as an example. The only limit is what role and policy are assigned to this MSI token.
    for resource_group in resource_client.resource_groups.list():
        resource_group_name=resource_group.name
        print(resource_group_name + " " + subscription_name)

    #if you like to scan all resources
    #for resource in resource_client.resources.list():
       
    #using filters to limit resource to one resource type
    #Storage account
    #for resource in resource_client.resources.list(filter="resourceType eq 'Microsoft.Storage/storageAccounts'"):
    
    #Virtual machines
    for resource in resource_client.resources.list(filter="resourceType eq 'Microsoft.Compute/virtualMachines'"):
        i+=1
        print(str(i) + ":" + resource.name + " " + resource.type)
        print(resource)
