

# I. Web service
### 1.concept
Web service is a standardized medium to propagate communication between the client and server applications on the World Wide Web.
A web service is a software module which is designed to perform a certain set of tasks.
    • The web services can be searched for over the network and can also be invoked accordingly.
    • When invoked the web service would be able to provide functionality to the client which invokes that web service.
![alt](https://www.guru99.com/images/3-2016/032316_0646_Webservicea1.png)
 Fingure 1. Web Service Architecture Diagram

The above diagram shows a very simplistic view of how a web service would actually work. The client would invoke a series of web service calls via requests to a server which would host the actual web service.
These requests are made through what is known as remote procedure calls. Remote Procedure Calls(RPC) are calls made to methods which are hosted by the relevant web service.
The main component of a web service is the data which is transferred between the client and the server, and that is XML (Extensible markup language).
--> So when applications talk to each other, they actually talk in XML. This provides a common platform for application developed in various programming languages to talk to each other.
	There are mainly two types of web services.
        1. SOAP web services.
        2. RESTful web services.
	In order for a web service to be fully functional, there are certain components that need to be in place. These components need to be present irrespective of whatever development language is used for programming the web service.
### 2.WSDL (Web services description language)
A web service cannot be used if it cannot be found. The client invoking the web service should know where the web service actually resides.
The client application needs to know what the web service actually does, so that it can invoke the right web service. By using the WSDL document, the client application would be able to understand where the web service is located and how it can be utilized.

An example of a WSDL file :
```sh
<definitions>	
   <message name="TutorialRequest">
      <part name="TutorialID" type="xsd:string"/>
   </message>
     
   <message name="TutorialResponse">
      <part name="TutorialName" type="xsd:string"/>
   </message>

   <portType name="Tutorial_PortType">
      <operation name="Tutorial">
         <input message="tns:TutorialRequest"/>
         <output message="tns:TutorialResponse"/>
      </operation>
   </portType>

   <binding name="Tutorial_Binding" type="tns:Tutorial_PortType">
      <soap:binding style="rpc"
         transport="http://schemas.xmlsoap.org/soap/http"/>
      <operation name="Tutorial">
         <soap:operation soapAction="Tutorial"/>
         <input>
            <soap:body
               encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
               namespace="urn:examples:Tutorialservice"
               use="encoded"/>
         </input>
		 <output>
            <soap:body
               encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
               namespace="urn:examples:Tutorialservice"
               use="encoded"/>
         </output>
      </operation>
   </binding>
</definitions>
```
<message> - The message parameter in the WSDL definition is used to define the different data elements for each operation performed by the web service. The TutorialRequest contains an element called "TutorialID" which is of the type string. Similarly, the TutorialResponse operation contains an element called "TutorialName" which is also a type string.
<portType> - This actually describes the operation which can be performed by the web service, which in our case is called Tutorial. This operation can take 2 messages; one is an input message, and the other is the output message.
<binding> - This element contains the protocol which is used. So in our case, we are defining it to use http (http://schemas.xmlsoap.org/soap/http). We also specify other details for the body of the operation, like the namespace and whether the message should be encoded.
### 3. Web Services Advantages
- Exposing Business Functionality on the network
- Interoperability amongst applications
- A Standardized Protocol which everybody understands
- Reduction in cost of communication
# II. RESTful API
-RESTful API is a standard used in designing APIs for web applications to manage resources. RESTful is one of the most commonly used API design types today to let different applications (web, mobile ...) communicate with each other.
- REST works primarily on the HTTP protocol. The above basic operations will use its own HTTP methods:
	GET (SELECT): This would be used to get a list of all employee using the RESTful web service 
	POST (CREATE): This would be used to create a new employee using the RESTful web service
    PUT (UPDATE): This would be used to update all employee using the RESTful web service
	DELETE (DELETE): This would be used to delete all employee using the RESTful web service
![alt](https://topdev.vn/blog/wp-content/uploads/2019/04/restful-rest-diagram-api.jpg)
Figure 2. How does RESTful work
### 1. Status code
All HTTP response status codes are separated into five classes or categories. The first digit of the status code defines the class of response, while the last two digits do not have any classifying or categorization role. There are five classes defined by the standard:
- 1xx informational response – the request was received, continuing process
- 2xx successful – the request was successfully received, understood, and accepted
- 3xx redirection – further action needs to be taken in order to complete the request
- 4xx client error – the request contains bad syntax or cannot be fulfilled
- 5xx server error – the server failed to fulfil an apparently valid request
### 2. JSON
JSON (JavaScript Object Notation) is most widely used data format for data interchange on the web. This data interchange can happen between two computers applications at different geographical locations or running within same hardware machine.
The good thing is that JSON is a human and machine readable format. So while applications/libraries can parse the JSON data – humans can also look at data and derive meaning from it.
A JSON document may contains text, curly braces, square brackets, colons, commas, double quotes, and maybe a few other characters.
Primarily, JSON is built on two structures:
A collection of name/value pairs. In various languages, this is realized as an object, record, struct, dictionary, hash table, keyed list, or associative array.
An ordered list of values. In most languages, this is realized as an array, vector, list, or sequence.


