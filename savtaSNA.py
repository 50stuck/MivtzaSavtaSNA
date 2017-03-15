import csv

savta_script = open("savta.txt", mode="r", encoding="utf-8")
scene_members = []

savta_network = open("savta.csv", mode="a", encoding="utf-8", newline="\n")
savta_writer = csv.writer(savta_network)

for line in savta_script:
    if len(line)>2:
        if line.find("-")>0:
            scene_members.append(line[line.find("-")+1:].strip('\n')[::-1])
    elif len(scene_members) > 0:
        for i in range(0, len(scene_members)-1):
            savta_writer.writerow([scene_members[i], scene_members[i+1]])
            #print(scene_members[i],"-",scene_members[i+1])
        scene_members = []

savta_script.close()
savta_network.close()