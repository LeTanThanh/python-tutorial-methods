from request import Request

if __name__ == "__main__":
  # Introduction to the Python methods

  """
  By definition, a method is a function that is bound to an instance of a class.
  This tutorial helps you understand how it works under the hood.

  The following defines a Request class that contains a function send():

  And you can call the send() function via the Request class like this:
  Be"""

  # Request.send()

  """
  The send() is a function object, which is an instance of the function class as shown in the following output:
  """

  # print(type(Request.send)) # <class 'function'>

  """
  The following creates a new instance of the Request class:
  """

  # request = Request()

  """
  If you display the request.send, it'll return a bound method object:
  """

  # print(type(request.send)) # <class 'method'>

  """
  So request.send is not a function like Request.send.
  The following checks Request.send is the same object as request.send.
  It'll returns False as expected:
  """

  # print(type(Request.send) is type(request.send)) # False

  """
  The reason is that the type of the Request.send is function while the type of the request.send is method, as shown below
  """

  # print(type(Request.send)) # <class 'function'>
  # print(type(request.send)) # <class 'method'>

  """
  So when you define a function inside a class, it's purely a function.
  However, when you access that function via an object, the function becomes a method.

  Therefore, a method is a function that is bound to an instance of a class.

  If you call the send() function via the request object, you'll get a TypeError as follows:
  """

  # request.send()
  # TypeError: Request.send() takes 0 positional arguments but 1 was given

  """
  Because the request is a method that is bound to the request object, Python always implicitly passes the object to the method as the first argument.

  The following redefines the Request class where the send function accepts a list of arguments:

  The following calls the send function from the Request class
  """

  # Request.send()  # Sent ()

  """
  The send() function doesn't receive any arguments.

  However, if you call the send() function from an instance of the Request class, the args is not empty:
  """

  # request = Request()
  # request.send()  # Sent (<request.Request object at 0x102b4ae10>,)

  """
  In this case, the send() method receives an object which is the request, which is the object that it is bound to.

  The following illustrates that the object that calls the send() method is the one that Python implicitly passes into the method as the first argument:
  """

  # request = Request()
  # print(hex(id(request)))
  # request.send()

  """
  The request object is the same as the one Python passes to the send() method as the first argument because they have the same memory address.
  In other words, you can access the instance of the class as the first argument inside the send() method:

  The following method call:
  """

  request = Request()
  request.send()

  """
  is equivalent to the following function call:
  """

  Request.send(request)

  """
  For this reason, a method of an object always has the object as the first argument.
  By convention, it is called self:
  """
