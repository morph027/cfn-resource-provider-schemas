SCHEMA = {
  "typeName" : "AWS::Wisdom::AIPromptVersion",
  "description" : "Definition of AWS::Wisdom::AIPromptVersion Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : { },
  "properties" : {
    "AIPromptArn" : {
      "type" : "string",
      "pattern" : "^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})?$"
    },
    "AssistantArn" : {
      "type" : "string",
      "pattern" : "^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})?$"
    },
    "AIPromptId" : {
      "type" : "string",
      "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$"
    },
    "AssistantId" : {
      "type" : "string",
      "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$"
    },
    "AIPromptVersionId" : {
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
  "required" : [ "AssistantId", "AIPromptId" ],
  "createOnlyProperties" : [ "/properties/AssistantId", "/properties/AIPromptId", "/properties/ModifiedTimeSeconds" ],
  "readOnlyProperties" : [ "/properties/AIPromptArn", "/properties/AIPromptVersionId", "/properties/AssistantArn", "/properties/VersionNumber" ],
  "primaryIdentifier" : [ "/properties/AssistantId", "/properties/AIPromptId", "/properties/VersionNumber" ],
  "additionalIdentifiers" : [ [ "/properties/AIPromptArn", "/properties/AssistantArn" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "wisdom:CreateAIPromptVersion" ]
    },
    "read" : {
      "permissions" : [ "wisdom:GetAIPrompt", "wisdom:GetAIPromptVersion" ]
    },
    "update" : {
      "permissions" : [ "wisdom:GetAIPrompt", "wisdom:GetAIPromptVersion" ]
    },
    "delete" : {
      "permissions" : [ "wisdom:DeleteAIPromptVersion" ]
    },
    "list" : {
      "permissions" : [ "wisdom:ListAIPromptVersions" ],
      "handlerSchema" : {
        "properties" : {
          "AssistantId" : {
            "$ref" : "resource-schema.json#/properties/AssistantId"
          },
          "AIPromptId" : {
            "$ref" : "resource-schema.json#/properties/AIPromptId"
          }
        },
        "required" : [ "AssistantId", "AIPromptId" ]
      }
    }
  }
}