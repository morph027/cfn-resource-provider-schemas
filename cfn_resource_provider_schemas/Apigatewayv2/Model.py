SCHEMA = {
  "typeName" : "AWS::ApiGatewayV2::Model",
  "description" : "The ``AWS::ApiGatewayV2::Model`` resource updates data model for a WebSocket API. For more information, see [Model Selection Expressions](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-expressions) in the *API Gateway Developer Guide*.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-apigatewayv2",
  "additionalProperties" : False,
  "properties" : {
    "ModelId" : {
      "type" : "string",
      "description" : ""
    },
    "Description" : {
      "type" : "string",
      "description" : "The description of the model."
    },
    "ContentType" : {
      "type" : "string",
      "description" : "The content-type for the model, for example, \"application/json\"."
    },
    "Schema" : {
      "type" : "object",
      "description" : "The schema for the model. For application/json models, this should be JSON schema draft 4 model."
    },
    "ApiId" : {
      "type" : "string",
      "description" : "The API identifier."
    },
    "Name" : {
      "type" : "string",
      "description" : "The name of the model."
    }
  },
  "required" : [ "ApiId", "Schema", "Name" ],
  "createOnlyProperties" : [ "/properties/ApiId" ],
  "primaryIdentifier" : [ "/properties/ApiId", "/properties/ModelId" ],
  "readOnlyProperties" : [ "/properties/ModelId" ],
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