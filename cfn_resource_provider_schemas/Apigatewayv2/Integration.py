SCHEMA = {
  "typeName" : "AWS::ApiGatewayV2::Integration",
  "additionalProperties" : False,
  "description" : "An example resource schema demonstrating some basic constructs and validation rules.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "ResponseParameter" : {
      "description" : "response parameter",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Destination" : {
          "type" : "string"
        },
        "Source" : {
          "type" : "string"
        }
      }
    },
    "ResponseParameterList" : {
      "description" : "list of response parameters",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/ResponseParameter"
      }
    },
    "ResponseParameterMap" : {
      "description" : "map of response parameter lists",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ResponseParameters" : {
          "$ref" : "#/definitions/ResponseParameterList"
        }
      }
    },
    "TlsConfig" : {
      "description" : "The TlsConfig property specifies the TLS configuration for a private integration. Supported only for HTTP APIs.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ServerNameToVerify" : {
          "type" : "string"
        }
      }
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "ApiId" : {
      "description" : "The API identifier.",
      "type" : "string"
    },
    "ConnectionId" : {
      "description" : "The ID of the VPC link for a private integration. Supported only for HTTP APIs.",
      "type" : "string"
    },
    "ConnectionType" : {
      "description" : "The type of the network connection to the integration endpoint. Specify INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and resources in a VPC. The default value is INTERNET.",
      "type" : "string"
    },
    "ContentHandlingStrategy" : {
      "description" : "Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT.",
      "type" : "string"
    },
    "CredentialsArn" : {
      "description" : "Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, don't specify this parameter.",
      "type" : "string"
    },
    "Description" : {
      "description" : "The description of the integration.",
      "type" : "string"
    },
    "IntegrationMethod" : {
      "description" : "Specifies the integration's HTTP method type.",
      "type" : "string"
    },
    "IntegrationSubtype" : {
      "description" : "Supported only for HTTP API AWS_PROXY integrations. Specifies the AWS service action to invoke.",
      "type" : "string"
    },
    "IntegrationId" : {
      "description" : "The integration ID.",
      "type" : "string"
    },
    "IntegrationType" : {
      "description" : "The integration type of an integration.",
      "type" : "string"
    },
    "IntegrationUri" : {
      "description" : "For a Lambda integration, specify the URI of a Lambda function. For an HTTP integration, specify a fully-qualified URL. For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service.",
      "type" : "string"
    },
    "PassthroughBehavior" : {
      "description" : "Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER. Supported only for WebSocket APIs.",
      "type" : "string"
    },
    "PayloadFormatVersion" : {
      "description" : "Specifies the format of the payload sent to an integration. Required for HTTP APIs. For HTTP APIs, supported values for Lambda proxy integrations are 1.0 and 2.0 For all other integrations, 1.0 is the only supported value.",
      "type" : "string"
    },
    "RequestParameters" : {
      "description" : "A key-value map specifying parameters.",
      "type" : "object",
      "additionalProperties" : False,
      "patternProperties" : {
        "[a-zA-Z0-9]+" : {
          "type" : "string"
        }
      }
    },
    "RequestTemplates" : {
      "description" : "A map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client.",
      "type" : "object",
      "additionalProperties" : False,
      "patternProperties" : {
        "[a-zA-Z0-9]+" : {
          "type" : "string"
        }
      }
    },
    "ResponseParameters" : {
      "description" : "Parameters that transform the HTTP response from a backend integration before returning the response to clients. Supported only for HTTP APIs.",
      "type" : "object",
      "additionalProperties" : False,
      "patternProperties" : {
        "[a-zA-Z0-9]+" : {
          "$ref" : "#/definitions/ResponseParameterMap"
        }
      }
    },
    "TemplateSelectionExpression" : {
      "description" : "The template selection expression for the integration. Supported only for WebSocket APIs.",
      "type" : "string"
    },
    "TimeoutInMillis" : {
      "description" : "Custom timeout between 50 and 29000 milliseconds for WebSocket APIs and between 50 and 30000 milliseconds for HTTP APIs. The default timeout is 29 seconds for WebSocket APIs and 30 seconds for HTTP APIs.",
      "type" : "integer"
    },
    "TlsConfig" : {
      "description" : "The TLS configuration for a private integration. If you specify a TLS configuration, private integration traffic uses the HTTPS protocol. Supported only for HTTP APIs.",
      "$ref" : "#/definitions/TlsConfig"
    }
  },
  "required" : [ "ApiId", "IntegrationType" ],
  "createOnlyProperties" : [ "/properties/ApiId" ],
  "readOnlyProperties" : [ "/properties/IntegrationId" ],
  "primaryIdentifier" : [ "/properties/ApiId", "/properties/IntegrationId" ],
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "apigateway:POST" ]
    },
    "update" : {
      "permissions" : [ "apigateway:PATCH", "apigateway:GET", "apigateway:PUT" ]
    },
    "read" : {
      "permissions" : [ "apigateway:GET" ]
    },
    "delete" : {
      "permissions" : [ "apigateway:GET", "apigateway:DELETE" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "ApiId" : {
            "$ref" : "resource-schema.json#/properties/ApiId"
          }
        },
        "required" : [ "ApiId" ]
      },
      "permissions" : [ "apigateway:GET" ]
    }
  }
}