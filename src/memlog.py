from datetime import datetime
import json


"""
Given a guild, updates the memlog file with details of all members in that guild.
List of changes are written to dump file and returned (crude).
Input:  - guild (class discord.Guild)
Output: - full_memlog (string): a string detailing all the changes done
"""
def memlog(guild):

    members = guild.members

    memlog_file = "data/memlog.json"
    changelog_file = "data/changelog.txt"
    
    full_memlog = f""

    with open(memlog_file, "r") as f:
        memdict = json.load(f)

    # if new server, create a new dict entry
    if str(guild.id) not in memdict:
        memdict[str(guild.id)] = dict()
    
    memdict_guild = memdict[str(guild.id)]
    
    timestamp = datetime.now()

    # loop through every member in the server
    for member in members:
        member_id = str(member.id)
        # if new member, create a new dict entry
        if (member_id not in memdict_guild):
            memdict_guild[member_id] = dict()
            memdict_guild[member_id]["server"] = 1
            memdict_guild[member_id]["name"] = member.name
            memdict_guild[member_id]["discriminator"] = member.discriminator
            memdict_guild[member_id]["roles"] = list()
            for role in member.roles:
                memdict_guild[member_id]["roles"].append(role.name)
            
            s = f"{timestamp} joined; "
            full_memlog += str(member.name).rjust(10) + " " + s 
            memdict_guild[member_id]["changelog"] = s

        # if not a new member
        else:
            # check if member is in the server
            if memdict_guild[member_id]["server"] != 1:
                s = f"{timestamp} joined; "
                full_memlog += str(member.name).rjust(10) + " " + s
                memdict_guild[member_id]["changelog"] += s
                memdict_guild[member_id]["server"] = 1

            # check if every property matches, if not then add change to log and update memdict
            if memdict_guild[member_id]["name"] != member.name:
                s = f"{timestamp} name {memdict_guild[member_id]['name']} -> {member.name}; ".encode('unicode-escape').decode('utf-8')
                full_memlog += str(member.name).rjust(10) + " " + s
                memdict_guild[member_id]["changelog"] += s
                memdict_guild[member_id]["name"] = member.name
            
            if memdict_guild[member_id]["discriminator"] != member.discriminator:
                s = f"{timestamp} discriminator {memdict_guild[member_id]['discriminator']} -> {member.discriminator}; "
                full_memlog += str(member.name).rjust(10) + " " + s
                memdict_guild[member_id]["changelog"] += s
                memdict_guild[member_id]["discriminator"] = member.discriminator
            
            for role in member.roles:
                if role.name not in memdict_guild[member_id]["roles"]:
                    s = f"{timestamp} role + {role.name}; ".encode('unicode-escape').decode('utf-8')
                    full_memlog += str(member.name).rjust(10) + " " + s
                    memdict_guild[member_id]["changelog"] += s
                    memdict_guild[member_id]["roles"].append(role.name)
            
            for rolename in memdict_guild[member_id]["roles"]:

                member_role_name_list = list()
                for role in member.roles:
                    member_role_name_list.append(role.name)
                
                if rolename not in member_role_name_list:
                    s = f"{timestamp} role - {rolename}; ".encode('unicode-escape').decode('utf-8')
                    full_memlog += str(member.name).rjust(10) + " " + s
                    memdict_guild[member_id]["changelog"] += s
                    memdict_guild[member_id]["roles"].remove(rolename)
    
    member_id_list = list()
    for member in members:
        member_id_list.append(str(member.id))
    
    # then loop through every single member in the dict to check if any have left
    for member in memdict_guild:
        if member not in member_id_list:
            if memdict_guild[member]["server"] != 0:
                s = f"{timestamp} left; ".encode('unicode-escape').decode('utf-8')
                full_memlog += str(memdict_guild[member]["name"]).rjust(10) + " " + s
                memdict_guild[member]["changelog"] += s
                memdict_guild[member]["server"] = 0

    with open(memlog_file, "w") as f:
        json.dump(memdict, f, indent=4)
    
    if full_memlog != "":
        full_memlog = guild.name + "= " + full_memlog + ";END; "
        with open(changelog_file, "a") as f:
            json.dump(full_memlog, f)
