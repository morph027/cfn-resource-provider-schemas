SCHEMA = {
  "typeName" : "AWS::CleanRooms::PrivacyBudgetTemplate",
  "description" : "Represents a privacy budget within a collaboration",
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "maxLength" : 200
    },
    "CollaborationArn" : {
      "type" : "string",
      "maxLength" : 100
    },
    "CollaborationIdentifier" : {
      "type" : "string",
      "maxLength" : 36,
      "minLength" : 36,
      "pattern" : "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    },
    "PrivacyBudgetTemplateIdentifier" : {
      "type" : "string",
      "maxLength" : 36,
      "minLength" : 36,
      "pattern" : "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    },
    "Tags" : {
      "description" : "An arbitrary set of tags (key-value pairs) for this cleanrooms privacy budget template.",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "type" : "array"
    },
    "AutoRefresh" : {
      "type" : "string",
      "enum" : [ "CALENDAR_MONTH", "NONE" ]
    },
    "PrivacyBudgetType" : {
      "type" : "string",
      "enum" : [ "DIFFERENTIAL_PRIVACY" ]
    },
    "Parameters" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Epsilon" : {
          "type" : "integer",
          "minimum" : 1,
          "maximum" : 20
        },
        "UsersNoisePerQuery" : {
          "type" : "integer",
          "minimum" : 10,
          "maximum" : 100
        }
      },
      "required" : [ "Epsilon", "UsersNoisePerQuery" ]
    },
    "MembershipArn" : {
      "type" : "string",
      "maxLength" : 100
    },
    "MembershipIdentifier" : {
      "type" : "string",
      "maxLength" : 36,
      "minLength" : 36,
      "pattern" : "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    }
  },
  "required" : [ "AutoRefresh", "PrivacyBudgetType", "Parameters", "MembershipIdentifier" ],
  "readOnlyProperties" : [ "/properties/CollaborationArn", "/properties/CollaborationIdentifier", "/properties/PrivacyBudgetTemplateIdentifier", "/properties/Arn", "/properties/MembershipArn" ],
  "createOnlyProperties" : [ "/properties/MembershipIdentifier", "/properties/PrivacyBudgetType", "/properties/AutoRefresh" ],
  "primaryIdentifier" : [ "/properties/PrivacyBudgetTemplateIdentifier", "/properties/MembershipIdentifier" ],
  "replacementStrategy" : "delete_then_create",
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "cleanrooms:ListTagsForResource", "cleanrooms:UntagResource", "cleanrooms:TagResource" ]
  },
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-cleanrooms",
  "handlers" : {
    "create" : {
      "permissions" : [ "cleanrooms:CreatePrivacyBudgetTemplate", "cleanrooms:ListTagsForResource", "cleanrooms:TagResource", "cleanrooms:GetPrivacyBudgetTemplate", "cleanrooms:ListPrivacyBudgetTemplates" ]
    },
    "read" : {
      "permissions" : [ "cleanrooms:GetPrivacyBudgetTemplate", "cleanrooms:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "cleanrooms:UpdatePrivacyBudgetTemplate", "cleanrooms:GetPrivacyBudgetTemplate", "cleanrooms:ListTagsForResource", "cleanrooms:TagResource", "cleanrooms:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "cleanrooms:DeletePrivacyBudgetTemplate", "cleanrooms:GetPrivacyBudgetTemplate", "cleanrooms:ListPrivacyBudgetTemplates", "cleanrooms:ListTagsForResource", "cleanrooms:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "cleanrooms:ListPrivacyBudgetTemplates" ],
      "handlerSchema" : {
        "properties" : {
          "MembershipIdentifier" : {
            "$ref" : "resource-schema.json#/properties/MembershipIdentifier"
          }
        },
        "required" : [ "MembershipIdentifier" ]
      }
    }
  },
  "additionalProperties" : False
}