SCHEMA = {
  "typeName" : "AWS::ApiGatewayV2::Deployment",
  "description" : "The ``AWS::ApiGatewayV2::Deployment`` resource creates a deployment for an API.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-apigatewayv2",
  "additionalProperties" : False,
  "properties" : {
    "DeploymentId" : {
      "type" : "string",
      "description" : ""
    },
    "Description" : {
      "type" : "string",
      "description" : "The description for the deployment resource."
    },
    "StageName" : {
      "type" : "string",
      "description" : "The name of an existing stage to associate with the deployment."
    },
    "ApiId" : {
      "type" : "string",
      "description" : "The API identifier."
    }
  },
  "required" : [ "ApiId" ],
  "createOnlyProperties" : [ "/properties/ApiId" ],
  "primaryIdentifier" : [ "/properties/ApiId", "/properties/DeploymentId" ],
  "readOnlyProperties" : [ "/properties/DeploymentId" ],
  "writeOnlyProperties" : [ "/properties/StageName" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags"
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