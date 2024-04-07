import os
import re
import subprocess
import xml.etree.ElementTree as ET

class CommandManual:     
    'class commandmanual is to fill the XML files with information'
    def __init__(self, command):
        self.command = command
        #get the information from each method 
        self.name=self.get_command_name()
        self.description = self.get_command_description()
        self.version = self.get_command_version() 
        self.example = self.get_command_example()
        self.related_commands = self.get_related_commands()
        #get description information for each command 

    def get_command_name(self):
         return self.command

    def get_command_description(self):
            comm = f"man {self.command}" 
            #exexute linux command and get the output
            result = subprocess.run(comm, shell=True, capture_output=True, text=True)
            if result.returncode == 0: #check if there a result output
                desc = result.stdout #let resutls store here
                description_match = re.search(r"DESCRIPTION", desc) #get the section that contaion the description
               
               #get the value of discription
                if description_match:
                    description_start = description_match.start()
                    description_line_end = desc.find('\n', description_start)

                    if  self.command=="touch" or self.command=="ls" or self.command=="sort" or self.command=="cut" or self.command=="mkdir" :
                        marker_line = "Mandatory"
                        check = desc.find(marker_line, description_line_end) #let the description stop here
                        lines_between_desc_check = desc[description_start:check]
                        return lines_between_desc_check #value of description for the command
                    
                    elif self.command=="man":
                        #get the end of description
                        marker_line = "The table below shows the section"
                        check = desc.find(marker_line, description_line_end)
                        lines_between_desc_check = desc[description_start:check]
                        return lines_between_desc_check
                    
                    elif self.command=="grep" or self.command=="find" or self.command=="rm":
                        #get the end of description
                        marker_line = "OPTIONS"
                        check = desc.find(marker_line, description_line_end)
                        lines_between_desc_check = desc[description_start:check]
                        return lines_between_desc_check
    
                    else:
                        marker_line = "\n\n" #for command that have one line description
                         #get the end of description

                        check = desc.find(marker_line, description_line_end)
                        lines_between_desc_check = desc[description_start:check]
                        return lines_between_desc_check
                    
                else:
                    print("these is no descriopn in the manual page")
                    return None
                
    def get_command_version(self):
        #get the version for each command 

        if self.command=="echo" or self.command=="pwd":
            comm = f"/bin/{self.command} --version"
            #to exacute the linux command
            result = subprocess.run(comm, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                    #to get the first line of it just
                    ver = result.stdout.strip().split('\n')[0]
                    return ver
        else:
            comm = f"{self.command} --version"
                 #to exacute the linux command
            result = subprocess.run(comm, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                    #to get the first line of it just
                    ver = result.stdout.strip().split('\n')[0]
                    return ver
            
    def get_command_example(self):
            #to get the example for each commmand
            if self.command=="man":
                comm = f"man {self.command}"
                                 #to exacute the linux command
                result = subprocess.run(comm, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    example = result.stdout
                    #start reading from EXAMPLES
                    example_match = re.search(r"EXAMPLES", example)
                    if example_match:
                        example_start = example_match.start()

                        example_line_end = example.find('\n', example_start)

                        marker_line = "man man.7" #stop reading here 
                        check = example.find(marker_line, example_line_end)
                        lines_between_example_check = example[example_start:check]
                        return lines_between_example_check 
                    

            elif self.command=="ls":
                comm = f"{self.command}"
                extra = "\nthe command is 'ls'\n"  # Include the print statement
                #to execute the linux command
                result = subprocess.run(comm, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    example =result.stdout
                    example= extra +example
                    return example
                
            elif self.command=="touch":
                comm = f"{self.command} ahmad1201170.txt"
                extra = "\nthe command is 'touch ahmad1201170.txt'\n"  
                #to exexute  the command and ls the result1 to exexute if the command add the file
                result= subprocess.run(comm, shell=True, capture_output=True, text=True)
                result1= subprocess.run("ls", shell=True, capture_output=True, text=True)
                if result1.returncode == 0:
                    
                    example = result1.stdout
                    example= extra +example
                    return example 
                
              
            elif self.command=="rm":
                comm = f"{self.command} ahmad1201170.txt"
                extra = "\nthe command is 'rm ahmad1201170.txt'\n"  
                comm1 = "ls"
                result = subprocess.run(comm, shell=True, capture_output=True, text=True)
                result1 = subprocess.run(comm1, shell=True, capture_output=True, text=True)
                if result1.returncode == 0:
                    example = result1.stdout
                    example= extra +example
                    return example  
                  
            elif self.command=="sort":
                comm1=f"ls -l | {self.command}" 
                extra = "\nthe command is 'ls -l | sort.txt'\n"  
                result = subprocess.run(comm1, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    example = result.stdout
                    example= extra +example
                    return example 
                       
            elif self.command=="tr":
                extra = "\nthe command is 'tr '[a-z]' '[A-Z]''\n"  
                my_string = "hello world"
                capitalized_string = my_string.upper()
                example = capitalized_string
                example= extra +example
                return example  

            elif self.command=="pwd":
                comm = f"{self.command}"
                extra = "\nthe command is 'pwd'\n"  
                result = subprocess.run(comm, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    example = result.stdout
                    example= extra +example
                    return example 
 
            elif self.command=="cut":
                from datetime import datetime
                current_time = datetime.now().time()
                comm = f"echo {current_time} | {self.command} -d'.' -f1"
                extra = "\nthe command is 'echo date | cut -d'.' -f1'\n"  
                result = subprocess.run(['bash', '-c',comm], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if result.returncode == 0:
                    example = result.stdout
                    example= extra +example
                    return example  
            elif self.command=="echo":
                comm = f"{self.command} ahmad_ghazawneh 1201170"
                extra = "\nthe command is 'echo ahmad_ghazawneh 1201170'\n"  
                result = subprocess.run(comm, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    example = result.stdout
                    example= extra +example     
                    return example 
            elif self.command=="cat":
                comm = f"man {self.command}"
                result = subprocess.run(comm, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    example = result.stdout
                    example_match = re.search(r"EXAMPLES", example)
                    if example_match:
                        example_start = example_match.start()

                        example_line_end = example.find('\n', example_start)

                        marker_line = "AUTHOR"
                        check = example.find(marker_line, example_line_end)
                        lines_between_example_check = example[example_start:check]
                        return lines_between_example_check
                     
            elif self.command=="find":
                    comm = f"{self.command} ls_manual.xml"
                    extra = "\nthe command is 'find ls_manual.xml'\n"  
                    result = subprocess.run(comm, shell=True, capture_output=True, text=True)
                    if result.returncode == 0:
                        example = result.stdout
                        example= extra +example     
                        return example 
        
            elif self.command=="mkdir":
                    comm = f"{self.command} delete_dir"
                    extra = "\nthe command is 'mkdir delete_dir'\n"  
                    result= subprocess.run(comm, shell=True, capture_output=True, text=True)
                    result1= subprocess.run("ls", shell=True, capture_output=True, text=True)
                    if result1.returncode == 0:
                        example = result1.stdout
                        example= extra +example     
                        return example 
                    
            elif self.command=="rmdir":
                    comm = f"{self.command} delete_dir"
                    extra = "\nthe command is 'rmdir delete_dir'\n"  
                    
                    result= subprocess.run(comm, shell=True, capture_output=True, text=True)
                    result1= subprocess.run("ls", shell=True, capture_output=True, text=True)
                    if result1.returncode == 0:
                        example = result1.stdout
                        example= extra +example     
                        return example 
            elif self.command=="tail":
                
                    comm = f"{self.command} -10 example.txt"
                    extra = "\nthe command is 'tail -10 example.txt'\n"  
                    result= subprocess.run(comm, shell=True, capture_output=True, text=True)
                    if result.returncode == 0:
                        example = result.stdout
                        example= extra +example     
                        return example         
            else:
                comm = f"man {self.command}"
                result = subprocess.run(comm, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    example = result.stdout
                    example_match = re.search(r"EXAMPLE", example)
                    if example_match:
                        example_start = example_match.start()
                        example_line_end = example.find('\n', example_start)

                        marker_line = "SEE ALSO"
                        check = example.find(marker_line, example_line_end)
                        lines_between_example_check = example[example_start:check]
                        return lines_between_example_check
                                        
    def get_related_commands(self):
            result = subprocess.run(['bash', '-c', f"compgen -c {self.command}"],
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                related = result.stdout
                return related
    
  
class XmlSerializer:
    'this class is used to serilaized command manual into XML string'
    def __init__(self, command_manual):
        self.command_manual = command_manual

    def serialize(self):
        command_element = ET.Element('commandmanual')
        ET.SubElement(command_element, 'command_name').text = self.command_manual.name
        ET.SubElement(command_element, 'description').text = self.command_manual.description
        ET.SubElement(command_element, 'version').text = self.command_manual.version
        ET.SubElement(command_element, 'example').text = self.command_manual.example
        ET.SubElement(command_element, 'related_commands').text = self.command_manual.related_commands
        xml_string = ET.tostring(command_element, encoding='utf-8').decode()
        return xml_string

class CommandManualGenerator:
    'this class is to read the commands from a file and to create the manual of the command than come from the CommandManual class(Generate manual)'
    def __init__(self, input_file):
        self.input_file = input_file

    def main(self):
        #read the command from an input file
        with open(self.input_file, 'r') as file:
            commands = file.read().splitlines()
        for command in commands:
            #instance of each command to get the information of the command
            command_manual = CommandManual(command)
            #instance of the the class XmlSerializer
            xml_serializer = XmlSerializer(command_manual)
            #to let the information be as xml string
            xml_string = xml_serializer.serialize()
            #open the file and fill it
            with open(f"{command}_manual.xml", "w") as xml_file:
                xml_file.write(xml_string)

        print("the files are done successfully")                                   
class Work_space:
    'this class contain the menu and the operation from user'
    def __init__(self):
        self.choices = {
            '1': 'man', '2': 'ls', '3': 'touch', '4': 'rm', '5': 'sort','6': 'tr', '7': 'pwd',
            '8': 'cut', '9': 'echo', '10': 'cat','11': 'find', '12': 'mkdir', '13': 'rmdir',
            '14': 'tail', '15': 'grep'
        }
    def start(self):
        while True:
            
            check= [
            'man', 'ls', 'touch', 'rm', 'sort', 'tr', 'pwd',
            'cut', 'echo', 'cat', 'find', 'mkdir', 'rmdir',
            'tail', 'grep'
                 ]
            
              
            print("\n1)View\t2)verification\t3)search\n0) Exit")
            first_choice = input("Enter your choice:\n")
            #View the command operation   
            if first_choice=='1':
                while True:
                    print("\n1) man\t2) ls\t3) touch\t4) rm\t5) sort\t6) tr\t7) pwd\n8) cut\t9) echo\t10) cat\t11) find\t12) mkdir\t13) rmdir\t14) tail\t15) grep\n0) Exit")
                    choice = input("Enter a command to view :\n")
                    #return back
                    if choice == '0':
                        break

                    #get the command
                    filename = self.choices.get(choice)
                    if filename is None: #if the choice not one of them
                        print("\n\nPlease try again.[the choice you made not exist]")
                    else:
                        try: #to catch if this name exist
                            # Open the XML file 
                            with open(f"{filename}_manual.xml", 'r') as xml_file:
                                xml_content = xml_file.read()
                                print(xml_content)
                                same=[] # list for the recommened command
                                for j in check:
                                    with open(f"{j}_manual.xml", 'r') as xml_file:
                                         xml_content1 = xml_file.read()
                                         if filename=='grep' or filename=='find' or filename=='man':
                                            match = re.search(r"search", xml_content1)
                                            if match:
                                                #print(f"the keyword {userr} is in file {i}")
                                                same.append(f"{j}")
                                         if filename=='touch':
                                            match = re.search(r"Create", xml_content1)
                                            if match:
                                                same.append(f"{j}")  


                                         if filename=='rm':
                                            match = re.search(r"Remove", xml_content1)
                                            if match:
                                                #print(f"the keyword {userr} is in file {i}")
                                                same.append(f"{j}") 
                                         if filename=='rmdir':
                                            match = re.search(r"remove", xml_content1)
                                            if match:
                                                #print(f"the keyword {userr} is in file {i}")
                                                same.append(f"{j}")
                                         if filename=='mkdir':
                                            match = re.search(r"Update", xml_content1)
                                            if match:
                                                #print(f"the keyword {userr} is in file {i}")
                                                same.append(f"{j}")        
                                                       

                                         if filename=='pwd' or filename=='cut' or filename=='tail':
                                            match = re.search(r"Print", xml_content1)
                                            if match:
                                                #print(f"the keyword {userr} is in file {i}")
                                                same.append(f"{j}") 

                                if same:
                                    if filename in same:
                                         same.remove(f"{filename}")
                                    print("\n\nyou can try one of these recommended command: ",same)        
                                else:
                                    pass
                                   
                        
                                            #file not found
                        except FileNotFoundError:
                            print(f"Error: File '{filename}' not found.")

            #for the verification choice
            elif first_choice=='2':
          
              check= [
            'man', 'ls', 'touch', 'rm', 'sort', 'tr', 'pwd',
            'cut', 'echo', 'cat', 'find', 'mkdir', 'rmdir',
            'tail', 'grep'
                 ]
              
             
              for i in check:
                if i=="echo" or i=="pwd":
                 comm = f"/bin/{i} --version"
                else:
                 comm = f"{i} --version"
                result = subprocess.run(comm, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    ver = result.stdout.strip().split('\n')[0]
                    with open(f"{i}_manual.xml", 'r') as xml_file:
                                xml_content = xml_file.read()
                                version_match = re.search(r"<version>", xml_content)
                                if version_match:
                                    version_start = version_match.start()
                                    version_line_end = xml_content.find('', version_start)
                                    marker_line = "</version>"
                                    check = xml_content.find(marker_line, version_line_end)
                                    remove_from = '<version>'
                                    lines_between_version_check = xml_content[version_start + len(remove_from):check]
                                if lines_between_version_check == ver:
                                        print(f"The version for {i} is the same")
                                else:
                                        print(f"the version for {i} is not the same") 
                                        print("the real output for version is-->",lines_between_version_check)
             
                                        print("\nthe Templete output for version is-->",ver)
              print("______________________________________________________")        
              
              check= [
            'man', 'ls', 'touch', 'rm', 'sort', 'tr', 'pwd',
            'cut', 'echo', 'cat', 'find', 'mkdir', 'rmdir',
            'tail', 'grep'
                 ]
            
             
              for i in check:
                comm = f"man {i}"
                result = subprocess.run(comm, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    desc = result.stdout
                    description_match = re.search(r"DESCRIPTION", desc)
                    if description_match:

                        description_start = description_match.start()

                        description_line_end = desc.find('\n', description_start)


                    if  i=="touch" or i=="ls" or i=="sort" or i=="cut" or i=="mkdir" :
                        marker_line = "Mandatory"
                        check = desc.find(marker_line, description_line_end)
                        lines_between_description_check1 = desc[description_start:check]
                    elif i=="man":
                        marker_line = "The table below shows the section"
                        check = desc.find(marker_line, description_line_end)
                        lines_between_description_check1 = desc[description_start:check]
                    
                    elif i=="grep" or i=="find" or i=="rm":
                        marker_line = "OPTIONS"
                        check = desc.find(marker_line, description_line_end)
                        lines_between_description_check1 = desc[description_start:check]
    
                    else:
                        marker_line = "\n\n"
                        check = desc.find(marker_line, description_line_end)
                        lines_between_description_check1 = desc[description_start:check]
                    with open(f"{i}_manual.xml", 'r') as xml_file:
                                    xml_content = xml_file.read()
                                    description_match = re.search(r"<description>", xml_content)
                                    if description_match:
                                        description_start = description_match.start()
                                        description_line_end = xml_content.find('', description_start)
                                        marker_line = "</description>"
                                        check = xml_content.find(marker_line, description_line_end)
                                        remove_from = '<description>'
                                        lines_between_description_check = xml_content[description_start + len(remove_from):check]
                                    if lines_between_description_check == lines_between_description_check1:
                                            print(f"The description for {i} is the same")
                                    else:
                                            print(f"the description for {i} is not the same") 
                                            print("the real output for descriprion is-->",lines_between_description_check1)
                                            print("\nthe Templete output for descriotion is-->",lines_between_description_check)                          
              print("______________________________________________________")    
              check= [
            'man', 'ls', 'touch', 'rm', 'sort', 'tr', 'pwd',
            'cut', 'echo', 'cat', 'find', 'mkdir', 'rmdir',
            'tail', 'grep'
                 ]
              for i in check:
                if i=="man":
                    comm = f"man {i}"
                    result = subprocess.run(comm, shell=True, capture_output=True, text=True)
                    if result.returncode == 0:
                        example = result.stdout
                        example_match = re.search(r"EXAMPLES", example)
                        if example_match:
                            example_start = example_match.start()

                            example_line_end = example.find('\n', example_start)

                            marker_line = "man man.7"
                            check = example.find(marker_line, example_line_end)
                            lines_between_example_check = example[example_start:check]
                elif i=="ls":
                    comm = f"{i}"
                    extra = "\nthe command is 'ls'\n" 
                    result = subprocess.run(comm, shell=True, capture_output=True, text=True)
                    if result.returncode == 0:
                        example =result.stdout
                        example=extra + example
                        lines_between_example_check = example

                elif i=="touch": 
                    comm = f"{i} ahmad1201170.txt"
                    extra = "\nthe command is 'touch ahmad1201170.txt'\n"  
                    result= subprocess.run(comm, shell=True, capture_output=True, text=True)
                    result1= subprocess.run("ls", shell=True, capture_output=True, text=True)
                    if result1.returncode == 0:
                        
                        example = result1.stdout
                        example=extra + example
                        lines_between_example_check = example
                
                elif i=="rm":
                    comm = f"{i} ahmad1201170.txt"
                    extra = "\nthe command is 'rm ahmad1201170.txt'\n"  
                    comm1 = "ls"
                    result = subprocess.run(comm, shell=True, capture_output=True, text=True)
                    result1 = subprocess.run(comm1, shell=True, capture_output=True, text=True)
                    if result1.returncode == 0:
                        example = result1.stdout
                        example=extra + example
                        lines_between_example_check = example
                    
                elif i=="sort":
                    comm1=f"ls -l | {i}" 
                    extra = "\nthe command is 'ls -l | sort'\n"  
                    result = subprocess.run(comm1, shell=True, capture_output=True, text=True)
                    if result.returncode == 0:
                        example = result.stdout
                        example=extra + example
                        lines_between_example_check = example
                        
                elif i=="tr":
                    extra = "\nthe command is 'tr '[a-z]' '[A-Z]''\n"  
                    my_string = "hello world"
                    capitalized_string = my_string.upper()
                    example = capitalized_string
                    example=extra + example
                    lines_between_example_check = example

                elif i=="pwd":
                    comm = f"{i}"
                    extra = "\nthe command is 'pwd'\n"  

                    result = subprocess.run(comm, shell=True, capture_output=True, text=True)
                    if result.returncode == 0:
                        example = result.stdout
                        example=extra + example
                        lines_between_example_check = example
    
                elif i=="cut":
                    from datetime import datetime
                    current_time = datetime.now().time()
                    comm = f"echo {current_time} | {i} -d'.' -f1"
                    extra = "\nthe command is 'echo date | cut -d'.' -f1'\n"  
                    result = subprocess.run(['bash', '-c',comm], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    if result.returncode == 0:
                        example = result.stdout
                        example=extra + example
                        lines_between_example_check = example
                elif i=="echo":
                    comm = f"{i} ahmad_ghazawneh 1201170"
                    extra = "\nthe command is 'echo ahmad_ghazawneh 1201170'\n"  
                    result = subprocess.run(comm, shell=True, capture_output=True, text=True)
                    if result.returncode == 0:
                        example = result.stdout
                        example=extra + example
                        lines_between_example_check = example
                elif i=="cat":
                    comm = f"man {i}"
                    result = subprocess.run(comm, shell=True, capture_output=True, text=True)
                    if result.returncode == 0:
                        example = result.stdout
                        example_match = re.search(r"EXAMPLES", example)
                        if example_match:
                            example_start = example_match.start()
                            example_line_end = example.find('\n', example_start)
                            marker_line = "AUTHOR"
                            check = example.find(marker_line, example_line_end)
                            lines_between_example_check = example[example_start:check]
                        
                elif i=="find":
                        comm = f"{i} ls_manual.xml"
                        extra = "\nthe command is 'find ls_manual.xml'\n"  
                        result = subprocess.run(comm, shell=True, capture_output=True, text=True)
                        if result.returncode == 0:
                            example = result.stdout
                            example=extra + example
                            lines_between_example_check = example
            
                elif i=="mkdir":
                        comm = f"{i} delete_dir"
                        extra = "\nthe command is 'mkdir delete_dir'\n"  
                        result= subprocess.run(comm, shell=True, capture_output=True, text=True)
                        result1= subprocess.run("ls", shell=True, capture_output=True, text=True)
                        if result1.returncode == 0:
                            example = result1.stdout
                            example=extra + example
                            lines_between_example_check = example
                        
                elif i=="rmdir":
                        comm = f"{i} delete_dir"
                        extra = "\nthe command is 'rmdir delete_dir'\n"  
                        result= subprocess.run(comm, shell=True, capture_output=True, text=True)
                        result1= subprocess.run("ls", shell=True, capture_output=True, text=True)
                        if result1.returncode == 0:
                            example = result1.stdout
                            example=extra + example
                            lines_between_example_check = example
                elif i=="tail":
                        comm = f"{i} -10 example.txt"
                        extra = "\nthe command is 'tail -10 example.txt'\n"  
                        result= subprocess.run(comm, shell=True, capture_output=True, text=True)
                        if result.returncode == 0:
                            example = result.stdout
                            example=extra + example
                            lines_between_example_check = example
                else:
                    comm = f"man {i}"
                    result = subprocess.run(comm, shell=True, capture_output=True, text=True)
                    if result.returncode == 0:
                        example = result.stdout
                        example_match = re.search(r"EXAMPLE", example)
                        if example_match:
                            example_start = example_match.start()
                            example_line_end = example.find('\n', example_start)
                            marker_line = "SEE ALSO"
                            check = example.find(marker_line, example_line_end)
                            lines_between_example_check = example[example_start:check]
                with open(f"{i}_manual.xml", 'r') as xml_file:
                                    xml_content = xml_file.read()
                                    example_match = re.search(r"<example>", xml_content)
                                    if example_match:
                                        example_start = example_match.start()
                                        example_line_end = xml_content.find('', example_start)
                                        marker_line = "</example>"
                                        check = xml_content.find(marker_line, example_line_end)
                                        remove_from = '<example>'
                                        lines_between_example_check1 = xml_content[example_start + len(remove_from):check]
                                    if lines_between_example_check == lines_between_example_check1:
                                            print(f"The example for {i} is the same")
                                            
                                    else:
                                            print(f"the example for {i} is not the same") 
                                            print("the real output for example is-->",lines_between_example_check)
                                            print("\nthe Templete output for example is-->",lines_between_example_check1)                          
              print("______________________________________________________")    

              check= [
            'man', 'ls', 'touch', 'rm', 'sort', 'tr', 'pwd',
            'cut', 'echo', 'cat', 'find', 'mkdir', 'rmdir',
            'tail', 'grep'
                 ]
              for i in check:  
                result = subprocess.run(['bash', '-c', f"compgen -c {i}"],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if result.returncode == 0:
                    related = result.stdout
                with open(f"{i}_manual.xml", 'r') as xml_file:
                                        xml_content = xml_file.read()
                                        related_match = re.search(r"<related_commands>", xml_content)
                                        if related_match:
                                            related_start = related_match.start()
                                            related_line_end = xml_content.find('', related_start)
                                            marker_line = "</related_commands>"
                                            check = xml_content.find(marker_line, related_line_end)
                                            remove_from = '<related_commands>'
                                            lines_between_related_check1 = xml_content[related_start + len(remove_from):check]
                                        if related == lines_between_related_check1:
                                                print(f"The related command for {i} is the same")
                                                
                                        else:
                                                print(f"the related command for {i} is not the same") 
                                                print("the real output for related command is-->",related)
                                                print("\nthe Templete output for related command is-->",lines_between_related_check1)                          
              print("______________________________________________________")                    


            elif first_choice=='3':
              while True:   
                print("\n1)search for a command\t2)search a keyword in the command file\n0)Exit") 
                user=input("enter your choice: ")
                if user=='1':
                    userr=input("enter your command: ")
                    if os.path.exists(f"{userr}_manual.xml"):
                        print(f"{userr} file is exists.")
                        user_open=input("Do you want to print inforamtion of the command file? (Y/N): ")
                        if user_open=='Y' or user_open=='y':     
                            with open(f"{userr}_manual.xml", 'r') as xml_file:
                                    xml_content = xml_file.read()
                                    print(xml_content)
                        else:
                             pass            
                    else:
                        print(f"{userr} file does not exist.")
                if user=='2':
                     check= [
            'man', 'ls', 'touch', 'rm', 'sort', 'tr', 'pwd',
            'cut', 'echo', 'cat', 'find', 'mkdir', 'rmdir',
            'tail', 'grep'
                 ]
                     outputt=[]
                     userr=input("enter your keyword: ")
                     for i in check:
                        with open(f"{i}_manual.xml", 'r') as xml_file:
                             xml_content = xml_file.read()
                             match = re.search(rf"{userr}", xml_content)
                             if match:
                                #print(f"the keyword {userr} is in file {i}")
                                outputt.append(f"{i}")
                             else:
                                  pass
                     print("the files that contain the keyword is-->",outputt)        
                             
                if user=='0':
                     break
            elif first_choice=='0': 
                break
            else:
                print("\n\nPlease try again.[the choice you made not exist]")
              
                  

if __name__ == "__main__":
    input_file = "commands.txt" 
    manual_generator = CommandManualGenerator(input_file)
    manual_generator.main()
    manual_generator= Work_space()
    manual_generator.start()