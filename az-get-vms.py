from msrestazure.azure_active_directory import MSIAuthentication
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient
import json

# Create MSI Authentication
credentials = MSIAuthentication()


# Create a Subscription Client
subscription_client = SubscriptionClient(credentials)
subscription = next(subscription_client.subscriptions.list())
#print(subscription)

subscription_id = subscription.subscription_id

subscription_name = ""
rg_counter = 0
vm_counter = 0

vm_auto_start = False
vm_auto_stop = False
vm_premium_ssd = False
vm_start_time = ""
vm_stop_time = ""
vm_auto_chain = ""
vm_start_order = 0
vm_stop_order = 0


#Lookup in all subscriptions
for subscriptions in subscription_client.subscriptions.list():
    print(subscriptions.display_name)
    subscription_name = subscriptions.display_name
    subscription_id  = subscriptions.subscription_id

# Create a Resource Management client
    resource_client = ResourceManagementClient(credentials, subscription_id)

# List resource groups as an example. The only limit is what role and policy are assigned to this MSI token.
    #for resource_group in resource_client.resource_groups.list():
    #    rg_counter+=1
    #    resource_group_name=resource_group.name
    #    print("Resource group: Counter:" + str(rg_counter) + " Name: " + resource_group_name + " Subscription: " + subscription_name)

    #if you like to scan all resources
    #for resource in resource_client.resources.list():
       
    #using filters to limit resource to one resource type
       
    #Storage account
    #for resource in resource_client.resources.list(filter="resourceType eq 'Microsoft.Storage/storageAccounts'"):
    
    #Filter only virtual machines
    for resource in resource_client.resources.list(filter="resourceType eq 'Microsoft.Compute/virtualMachines'"):

        vm_counter+=1
        print("Virtual Machine No: " + str(vm_counter) + " Name: " + resource.name + " Resource Group: " + resource.type)
        tags = resource.tags
        #print(tags)
        
        if tags == None:
            print("No tags")
        else:

            if "Application" in tags:
                print("Application:" + tags["Application"])
            if "Owner" in tags:
                print("Owner:" + tags["Owner"])
            if "Environment" in tags:
                print("Environment:" + tags["Environment"])
            if "Project" in tags:
                print("Project:" + tags["Project"])
