SCHEMA = {
  "typeName" : "AWS::ApiGatewayV2::RouteResponse",
  "description" : "The ``AWS::ApiGatewayV2::RouteResponse`` resource creates a route response for a WebSocket API. For more information, see [Set up Route Responses for a WebSocket API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-route-response.html) in the *API Gateway Developer Guide*.",
  "additionalProperties" : False,
  "properties" : {
    "RouteResponseKey" : {
      "type" : "string",
      "description" : "The route response key."
    },
    "ResponseParameters" : {
      "$ref" : "#/definitions/RouteParameters",
      "description" : "The route response parameters."
    },
    "RouteId" : {
      "type" : "string",
      "description" : "The route ID."
    },
    "ModelSelectionExpression" : {
      "type" : "string",
      "description" : "The model selection expression for the route response. Supported only for WebSocket APIs."
    },
    "ApiId" : {
      "type" : "string",
      "description" : "The API identifier."
    },
    "ResponseModels" : {
      "type" : "object",
      "description" : "The response models for the route response."
    },
    "RouteResponseId" : {
      "type" : "string",
      "description" : ""
    }
  },
  "definitions" : {
    "ParameterConstraints" : {
      "type" : "object",
      "properties" : {
        "Required" : {
          "type" : "boolean",
          "description" : "Specifies whether the parameter is required."
        }
      },
      "required" : [ "Required" ],
      "additionalProperties" : False,
      "description" : "Specifies whether the parameter is required."
    },
    "RouteParameters" : {
      "patternProperties" : {
        "^.+$" : {
          "$ref" : "#/definitions/ParameterConstraints"
        }
      },
      "additionalProperties" : False
    }
  },
  "required" : [ "RouteResponseKey", "RouteId", "ApiId" ],
  "createOnlyProperties" : [ "/properties/ApiId", "/properties/RouteId" ],
  "readOnlyProperties" : [ "/properties/RouteResponseId" ],
  "primaryIdentifier" : [ "/properties/ApiId", "/properties/RouteId", "/properties/RouteResponseId" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
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
      "permissions" : [ "apigateway:GET" ]
    }
  }
}