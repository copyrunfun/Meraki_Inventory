import os
import meraki
import pandas as pd

meraki_api_key = os.environ.get('meraki_api_key')
dashboard = meraki.DashboardAPI(meraki_api_key)
my_orgs = dashboard.organizations.getOrganizations()
report = list()

for org in my_orgs:
    count = 0
    org_id = org['id']
    org_name = org['name']
    inventory = dashboard.organizations.getOrganizationInventoryDevices(org_id)
    for sub in inventory:
        location = sub['name']
        model = sub['model']
        if "Z" in model:
            count += 1
            report.append('- {} - {}'.format(location, model))
            print('- {} - {}'.format(location, model))
        elif "MX" in model:
            count += 1
            print('- {} - {}'.format(location, model))
            report.append('- {} - {}'.format(location, model))
    print('{} has {} managed firewall(s)'.format(org_name, count))
    report.append("{} has {} managed firewall(s)".format(org_name, count))
    report.append('--------------------------------------------------------')
print(report)

df = pd.DataFrame(report)

df.to_csv('report.csv', index=False)
