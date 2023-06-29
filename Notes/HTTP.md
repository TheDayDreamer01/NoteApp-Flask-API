| Status Code | Meaning                               | Description                                                                                                 |
|-------------|---------------------------------------|-------------------------------------------------------------------------------------------------------------|
| 1xx         | Informational                         |                                                                                                             |
| 100         | Continue                              | The initial part of a request has been received, and the client should proceed to send the remainder.        |
| 101         | Switching Protocols                   | The server confirms the client's request to switch protocols.                                               |
| 2xx         | Success                               |                                                                                                             |
| 200         | OK                                    | The request has succeeded.                                                                                  |
| 201         | Created                               | A new resource has been successfully created as a result of the request.                                   |
| 202         | Accepted                              | The request has been accepted for processing, but the processing is not yet complete.                        |
| 204         | No Content                            | The server has successfully fulfilled the request, but there is no additional content to send in the response.|
| 3xx         | Redirection                           |                                                                                                             |
| 300         | Multiple Choices                      | The requested resource has multiple choices, each with its own URI, and the user must select one.            |
| 301         | Moved Permanently                     | The requested resource has been permanently moved to a new location.                                        |
| 302         | Found                                 | The requested resource has been temporarily moved to a different location.                                  |
| 304         | Not Modified                          | The client's cached version of the requested resource is still valid, and the server has not modified it.     |
| 4xx         | Client Errors                         |                                                                                                             |
| 400         | Bad Request                           | The server cannot understand the request due to invalid syntax.                                             |
| 401         | Unauthorized                          | The request requires user authentication.                                                                   |
| 403         | Forbidden                             | The server understood the request, but refuses to authorize it.                                             |
| 404         | Not Found                             | The requested resource could not be found on the server.                                                    |
| 405         | Method Not Allowed                    | The method specified in the request is not allowed for the resource.                                        |
| 5xx         | Server Errors                         |                                                                                                             |
| 500         | Internal Server Error                 | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable.|
| 501         | Not Implemented                       | The server does not support the functionality required to fulfill the request.                              |
| 502         | Bad Gateway                           | The server, acting as a gateway or proxy, received an invalid response from an upstream server.             |
| 503         | Service Unavailable                   | The server is currently unable to handle the request due to a temporary overload or maintenance.             |
| 504         | Gateway Timeout                       | The server, acting as a gateway or proxy, did not receive a timely response from an upstream server.         |
