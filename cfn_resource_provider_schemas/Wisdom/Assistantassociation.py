SCHEMA = {
  "typeName" : "AWS::Wisdom::AssistantAssociation",
  "description" : "Definition of AWS::Wisdom::AssistantAssociation Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk",
  "definitions" : {
    "AssociationData" : {
      "type" : "object",
      "properties" : {
        "KnowledgeBaseId" : {
          "type" : "string",
          "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$"
        }
      },
      "required" : [ "KnowledgeBaseId" ],
      "additionalProperties" : False
    },
    "AssociationType" : {
      "type" : "string",
      "enum" : [ "KNOWLEDGE_BASE" ]
    },
    "Tag" : {
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "maxLength" : 128,
          "minLength" : 1,
          "pattern" : "^(?!aws:)[a-zA-Z+-=._:/]+$",
          "type" : "string"
        },
        "Value" : {
          "maxLength" : 256,
          "minLength" : 1,
          "type" : "string"
        }
      },
      "required" : [ "Key", "Value" ],
      "type" : "object"
    }
  },
  "properties" : {
    "AssistantAssociationArn" : {
      "type" : "string",
      "pattern" : "^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})?$"
    },
    "AssistantArn" : {
      "type" : "string",
      "pattern" : "^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})?$"
    },
    "AssistantAssociationId" : {
      "type" : "string",
      "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$"
    },
    "AssistantId" : {
      "type" : "string",
      "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$"
    },
    "Association" : {
      "$ref" : "#/definitions/AssociationData"
    },
    "AssociationType" : {
      "$ref" : "#/definitions/AssociationType"
    },
    "Tags" : {
      "insertionOrder" : False,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "type" : "array"
    }
  },
  "required" : [ "Association", "AssociationType", "AssistantId" ],
  "readOnlyProperties" : [ "/properties/AssistantAssociationId", "/properties/AssistantAssociationArn", "/properties/AssistantArn" ],
  "createOnlyProperties" : [ "/properties/Association", "/properties/AssociationType", "/properties/AssistantId", "/properties/Tags" ],
  "primaryIdentifier" : [ "/properties/AssistantAssociationId", "/properties/AssistantId" ],
  "additionalIdentifiers" : [ [ "/properties/AssistantAssociationArn", "/properties/AssistantArn" ] ],
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "wisdom:TagResource" ]
  },
  "replacementStrategy" : "delete_then_create",
  "handlers" : {
    "create" : {
      "permissions" : [ "wisdom:CreateAssistantAssociation", "wisdom:TagResource" ]
    },
    "update" : {
      "permissions" : [ "wisdom:GetAssistantAssociation" ]
    },
    "read" : {
      "permissions" : [ "wisdom:GetAssistantAssociation" ]
    },
    "list" : {
      "permissions" : [ "wisdom:ListAssistantAssociations" ],
      "handlerSchema" : {
        "properties" : {
          "AssistantId" : {
            "$ref" : "resource-schema.json#/properties/AssistantId"
          }
        },
        "required" : [ "AssistantId" ]
      }
    },
    "delete" : {
      "permissions" : [ "wisdom:DeleteAssistantAssociation" ]
    }
  }
}