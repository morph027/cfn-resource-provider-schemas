SCHEMA = {
  "typeName" : "AWS::Greengrass::SubscriptionDefinition",
  "description" : "Resource Type definition for AWS::Greengrass::SubscriptionDefinition",
  "additionalProperties" : False,
  "properties" : {
    "LatestVersionArn" : {
      "type" : "string"
    },
    "Id" : {
      "type" : "string"
    },
    "Arn" : {
      "type" : "string"
    },
    "Name" : {
      "type" : "string"
    },
    "InitialVersion" : {
      "$ref" : "#/definitions/SubscriptionDefinitionVersion"
    },
    "Tags" : {
      "type" : "object"
    }
  },
  "definitions" : {
    "SubscriptionDefinitionVersion" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Subscriptions" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/Subscription"
          }
        }
      },
      "required" : [ "Subscriptions" ]
    },
    "Subscription" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Target" : {
          "type" : "string"
        },
        "Id" : {
          "type" : "string"
        },
        "Source" : {
          "type" : "string"
        },
        "Subject" : {
          "type" : "string"
        }
      },
      "required" : [ "Target", "Id", "Source", "Subject" ]
    }
  },
  "required" : [ "Name" ],
  "readOnlyProperties" : [ "/properties/LatestVersionArn", "/properties/Arn", "/properties/Id" ],
  "createOnlyProperties" : [ "/properties/InitialVersion" ],
  "primaryIdentifier" : [ "/properties/Id" ]
}