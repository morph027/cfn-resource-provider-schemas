SCHEMA = {
  "typeName" : "AWS::ApiGatewayV2::IntegrationResponse",
  "description" : "The ``AWS::ApiGatewayV2::IntegrationResponse`` resource updates an integration response for an WebSocket API. For more information, see [Set up WebSocket API Integration Responses in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-integration-responses.html) in the *API Gateway Developer Guide*.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-apigatewayv2.git",
  "additionalProperties" : False,
  "properties" : {
    "IntegrationResponseId" : {
      "description" : "",
      "type" : "string"
    },
    "ResponseTemplates" : {
      "description" : "The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.",
      "type" : "object"
    },
    "TemplateSelectionExpression" : {
      "description" : "The template selection expression for the integration response. Supported only for WebSocket APIs.",
      "type" : "string"
    },
    "ResponseParameters" : {
      "description" : "A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.{name}``, where name is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.{name}`` or ``integration.response.body.{JSON-expression}``, where ``{name}`` is a valid and unique response header name and ``{JSON-expression}`` is a valid JSON expression without the ``$`` prefix.",
      "type" : "object"
    },
    "ContentHandlingStrategy" : {
      "description" : "Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT``, with the following behaviors:\n  ``CONVERT_TO_BINARY``: Converts a response payload from a Base64-encoded string to the corresponding binary blob.\n  ``CONVERT_TO_TEXT``: Converts a response payload from a binary blob to a Base64-encoded string.\n If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.",
      "type" : "string"
    },
    "IntegrationId" : {
      "description" : "The integration ID.",
      "type" : "string"
    },
    "IntegrationResponseKey" : {
      "description" : "The integration response key.",
      "type" : "string"
    },
    "ApiId" : {
      "description" : "The API identifier.",
      "type" : "string"
    }
  },
  "required" : [ "ApiId", "IntegrationId", "IntegrationResponseKey" ],
  "createOnlyProperties" : [ "/properties/ApiId", "/properties/IntegrationId" ],
  "readOnlyProperties" : [ "/properties/IntegrationResponseId" ],
  "primaryIdentifier" : [ "/properties/ApiId", "/properties/IntegrationId", "/properties/IntegrationResponseId" ],
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "apigateway:POST" ]
    },
    "read" : {
      "permissions" : [ "apigateway:GET" ]
    },
    "update" : {
      "permissions" : [ "apigateway:PATCH", "apigateway:PUT", "apigateway:GET" ]
    },
    "delete" : {
      "permissions" : [ "apigateway:GET", "apigateway:DELETE" ]
    },
    "list" : {
      "permissions" : [ "apigateway:GET" ]
    }
  }
}