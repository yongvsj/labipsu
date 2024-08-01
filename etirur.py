class RealSubject:
    def request(self):
        return "RealSubject: Handling request."

class Proxy:
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        # Adding additional behavior (e.g., logging, access control)
        print("Proxy: Logging the request.")
        # Forwarding the request to the real subject (the modified view)
        return self._real_subject.request()

# Client code
real_subject = RealSubject()
proxy = Proxy(real_subject)

# Using the proxy to interact with the real subject
result = proxy.request()
print(result)
