SCHEMA = {
  "typeName" : "AWS::ApiGatewayV2::Stage",
  "description" : "Resource Type definition for AWS::ApiGatewayV2::Stage",
  "additionalProperties" : False,
  "properties" : {
    "DeploymentId" : {
      "type" : "string"
    },
    "Description" : {
      "type" : "string"
    },
    "AutoDeploy" : {
      "type" : "boolean"
    },
    "RouteSettings" : {
      "type" : "object"
    },
    "StageName" : {
      "type" : "string"
    },
    "StageVariables" : {
      "type" : "object"
    },
    "AccessPolicyId" : {
      "type" : "string"
    },
    "ClientCertificateId" : {
      "type" : "string"
    },
    "AccessLogSettings" : {
      "$ref" : "#/definitions/AccessLogSettings"
    },
    "Id" : {
      "type" : "string"
    },
    "ApiId" : {
      "type" : "string"
    },
    "DefaultRouteSettings" : {
      "$ref" : "#/definitions/RouteSettings"
    },
    "Tags" : {
      "type" : "object"
    }
  },
  "definitions" : {
    "AccessLogSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DestinationArn" : {
          "type" : "string"
        },
        "Format" : {
          "type" : "string"
        }
      }
    },
    "RouteSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DetailedMetricsEnabled" : {
          "type" : "boolean"
        },
        "LoggingLevel" : {
          "type" : "string"
        },
        "DataTraceEnabled" : {
          "type" : "boolean"
        },
        "ThrottlingBurstLimit" : {
          "type" : "integer"
        },
        "ThrottlingRateLimit" : {
          "type" : "number"
        }
      }
    }
  },
  "required" : [ "StageName", "ApiId" ],
  "createOnlyProperties" : [ "/properties/StageName", "/properties/ApiId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}