''' 
apple_apps
Collection of wrapper classes for working with Apple built in applications such as Messages, Calendar, and Contacts
'''
import applescript
import vobject

class Messages: 
    '''
    Class for controlling Messages App
    ''' 
    def send_message(participant,message,service_type="SMS"):
        phone = str(participant)

        if any(x.isalpha() for x in participant):
            #try:
                contact = Contacts.lookup_contact({"name":participant})
                phone = contact.tel.value
           # except Exception as e: print(e)
        script = '''
        tell application "Messages"
            set targetService to 1st account whose service type = {}
            set targetBuddy to participant "{}" of targetService
            send "{}" to targetBuddy
        end tell
            '''.format(service_type,phone, message)
        run_script = applescript.AppleScript(script)
        run_script.run()

class Contacts:
    class Person:
        def __init__(self,**properties):
            self.properties = properties
            # self.attributes = attributes
            self.firstname = self.properties["first_name"]
            self.lastname = self.properties["last_name"]
            self.name = " ".join([self.firstname,self.lastname])
             

        def save(self): pass

    def lookup_contact(properties:dict):
        script = 'tell application "Contacts"\n'\
                  'get the vcard of 1st person whose '
        if len(properties)>1:
            print(properties)
            print(list(properties.keys()))
            for key in list(properties.keys())[:-1]:
                print(key)
                script += f'{key} contains "{properties[key]}" and '
        script += f'{list(properties.keys())[-1]} contains "{list(properties.values())[-1]}"\n'
        script += 'end tell'
        
        run_script = applescript.AppleScript(script)
        person = vobject.readOne(run_script.run())
        return person
        
    def create_contact(self,person):
        pass
        
    def del_contact(self,person):
        pass 
        


# class Calendar: 

# class Facetime:

# class Music: 

	
