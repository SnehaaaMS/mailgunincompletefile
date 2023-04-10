import requests,json
#
class MailGun:
    def __init__(self,apikey):
        self.apikey=apikey

    def get_domains(self,params):
        return requests.get(
            "https://api.mailgun.net/v3/domains",
            auth=("api", self.apikey) ,
            params=params
        )

    def send_simple_message(self,data):
        return requests.post(
            "https://api.mailgun.net/v3/sandbox811f814a15f14558a38e57a544fc0836.mailgun.org/messages",
            auth=("api", self.apikey),
            data=data)

    def send_complex_message(self):
        return requests.post(
            "https://api.mailgun.net/v3/sandbox811f814a15f14558a38e57a544fc0836.mailgun.org/messages",
            auth=("api", self.apikey),
            files=[("attachment", ("test.jpg", open("files/test.jpg", "rb").read())),
                   ("attachment", ("test.txt", open("files/test.txt", "rb").read()))],
            data={"from": "Excited User <YOU@YOUR_DOMAIN_NAME>",
                  "to": "foo@example.com",
                  "cc": "baz@example.com",
                  "bcc": "bar@example.com",
                  "subject": "Hello",
                  "text": "Testing some Mailgun awesomness!",
                  "html": "<html>HTML version of the body</html>"})


    def create_mailing_list(self,data):
        return requests.post(
            "https://api.mailgun.net/v3/lists",
            auth=('api', self.apikey),
            data=data)


    def view_lists(self):
        return requests.get(
            "https://api.mailgun.net/v3/lists/pages",
            auth=('api', self.apikey))


    def remove_list(self):
        return requests.delete(
            "https://api.mailgun.net/v3/lists/LIST@sandbox811f814a15f14558a38e57a544fc0836.mailgun.org",
            auth=('api', self.apikey))


    def add_list_member(self,data):
        return requests.post(
            "https://api.mailgun.net/v3/lists/LIST@sandbox811f814a15f14558a38e57a544fc0836.mailgun.org/members",
            auth=('api', self.apikey),
            data=data)



    def list_members(self):
        return requests.get(
            "https://api.mailgun.net/v3/lists/LIST@sandbox811f814a15f14558a38e57a544fc0836.mailgun.org/members/pages",
            auth=('api', self.apikey))


    def update_member(self,data):
        return requests.put(
            ("https://api.mailgun.net/v3/lists/LIST@sandbox811f814a15f14558a38e57a544fc0836.mailgun.org/members"
             "/bar@example.com"),
            auth=('api', self.apikey),
            data=data)


    def remove_member(self):
        return requests.delete(
            ("https://api.mailgun.net/v3/lists/LIST@YOUR_DOMAIN_NAME/members"
             "/bar@example.com"),
            auth=('api', self.apikey))



apikey='752d1b9ae53103e7b1ca31fd411714b4-81bd92f8-748d5056'
obj = MailGun(apikey)


params={"skip": 0,
        "limit": 3}
result = obj.get_domains(params)
print(result.json())


data={"from": "Excited User <mailgun@sandbox811f814a15f14558a38e57a544fc0836.mailgun.org>",
                  "to": ["qx77r1aa2n@zipcatfish.com", "YOU@sandbox811f814a15f14558a38e57a544fc0836.mailgun.org"],
                  "subject": "Hello",
                  "text": "Testing Mailgun"
                  }
result = obj.send_simple_message(data)
print(result.json())


data={'address': 'LIST@sandbox811f814a15f14558a38e57a544fc0836.mailgun.org',
                  'description': "Mailgun developers list"
                  }

result = obj.create_mailing_list(data)
print(result.json())

result = obj.view_lists()
print(result.json())

result = obj.remove_list()
print(result.json())

data={'subscribed': True,
                  'address': 'first@example.com',
                  'name': 'fir st',
                  'description': 'Developer',
                  'vars': '{"age": 26}'}
result = obj.add_list_member(data)
print(result.json())

result = obj.list_members()
print(result.json())

data={'subscribed': False,
                  'name': 'Foo Bar'}
result = obj.update_member(data)
print(result.json())

result = obj.remove_list()
print(result.json())

