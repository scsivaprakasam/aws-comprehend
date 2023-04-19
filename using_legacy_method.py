import boto3
import re

x=0
y=0
Text = 'Hello! Zhang Wei, I am "John". Your AnyCompany Financial Services, "LLC" credit card account 1111-0000-1111-0008'
texts=[]
foundtext = []

client = boto3.client(service_name='comprehendmedical', region_name='us-west-2')
result = client.detect_phi(Text=Text)
mapped = len(result['Entities'])
print(f"Entities: {len(result['Entities'])}")
if mapped > 0:
    print("Entities found in Entities Attribute")
    entities = result['Entities']
else:
    print("Entities not Found")

for foundtext in entities:
    texts.append(foundtext['Text'])

print(texts)

findstring = Text.split(" ")


for x in range(len(findstring)):
    for y in range(len(texts)):
        # removedspl = findstring[x].replace(",","").replace(".","")
        # removedspl = re.sub("[!@#$%^&*()[]{};:,./<>?\|`~-=_+]", " ", findstring[x])
        # removedspl = filter(str.isalnum(findstring[x]))
        removedspl = re.sub('[^A-Za-z0-9\-]+', '', findstring[x])
        # print(f"After removing special characters: {removedspl}")
        if removedspl in texts[y]:
            findstring[x] = "*****"
        y += 1
    x += 1


print(' '.join(findstring))
