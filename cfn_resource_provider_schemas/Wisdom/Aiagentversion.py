SCHEMA = {
  "typeName" : "AWS::Wisdom::AIAgentVersion",
  "description" : "Definition of AWS::Wisdom::AIAgentVersion Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : { },
  "properties" : {
    "AIAgentArn" : {
      "type" : "string",
      "pattern" : "^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})?$"
    },
    "AssistantArn" : {
      "type" : "string",
      "pattern" : "^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})?$"
    },
    "AIAgentId" : {
      "type" : "string",
      "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$"
    },
    "AssistantId" : {
      "type" : "string",
      "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$"
    },
    "AIAgentVersionId" : {
      "type" : "string",
      "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$"
    },
    "VersionNumber" : {
      "type" : "number"
    },
    "ModifiedTimeSeconds" : {
      "type" : "number"
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "required" : [ "AssistantId", "AIAgentId" ],
  "createOnlyProperties" : [ "/properties/AssistantId", "/properties/AIAgentId", "/properties/ModifiedTimeSeconds" ],
  "readOnlyProperties" : [ "/properties/AIAgentVersionId", "/properties/AIAgentArn", "/properties/AssistantArn", "/properties/VersionNumber" ],
  "primaryIdentifier" : [ "/properties/AssistantId", "/properties/AIAgentId", "/properties/VersionNumber" ],
  "additionalIdentifiers" : [ [ "/properties/AIAgentArn", "/properties/AssistantArn" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "wisdom:CreateAIAgentVersion" ]
    },
    "read" : {
      "permissions" : [ "wisdom:GetAIAgent", "wisdom:GetAIAgentVersion" ]
    },
    "update" : {
      "permissions" : [ "wisdom:GetAIAgent", "wisdom:GetAIAgentVersion" ]
    },
    "delete" : {
      "permissions" : [ "wisdom:DeleteAIAgentVersion" ]
    },
    "list" : {
      "permissions" : [ "wisdom:ListAIAgentVersions" ],
      "handlerSchema" : {
        "properties" : {
          "AssistantId" : {
            "$ref" : "resource-schema.json#/properties/AssistantId"
          },
          "AIAgentId" : {
            "$ref" : "resource-schema.json#/properties/AIAgentId"
          }
        },
        "required" : [ "AssistantId", "AIAgentId" ]
      }
    }
  }
}