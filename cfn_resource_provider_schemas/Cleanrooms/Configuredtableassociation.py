SCHEMA = {
  "typeName" : "AWS::CleanRooms::ConfiguredTableAssociation",
  "description" : "Represents a table that can be queried within a collaboration",
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
    },
    "ConfiguredTableAssociationAnalysisRuleType" : {
      "type" : "string",
      "enum" : [ "AGGREGATION", "LIST", "CUSTOM" ]
    },
    "AllowedResultReceiver" : {
      "type" : "string",
      "minLength" : 12,
      "maxLength" : 12,
      "pattern" : "\\d+"
    },
    "AllowedResultReceivers" : {
      "type" : "array",
      "insertionOrder" : False,
      "minItems" : 0,
      "items" : {
        "$ref" : "#/definitions/AllowedResultReceiver"
      }
    },
    "AllowedAdditionalAnalysis" : {
      "type" : "string",
      "maxLength" : 256
    },
    "AllowedAdditionalAnalyses" : {
      "type" : "array",
      "insertionOrder" : False,
      "minItems" : 0,
      "maxItems" : 25,
      "items" : {
        "$ref" : "#/definitions/AllowedAdditionalAnalysis"
      }
    },
    "ConfiguredTableAssociationAnalysisRuleCustom" : {
      "type" : "object",
      "properties" : {
        "AllowedResultReceivers" : {
          "$ref" : "#/definitions/AllowedResultReceivers"
        },
        "AllowedAdditionalAnalyses" : {
          "$ref" : "#/definitions/AllowedAdditionalAnalyses"
        }
      },
      "additionalProperties" : False
    },
    "ConfiguredTableAssociationAnalysisRuleAggregation" : {
      "type" : "object",
      "properties" : {
        "AllowedResultReceivers" : {
          "$ref" : "#/definitions/AllowedResultReceivers"
        },
        "AllowedAdditionalAnalyses" : {
          "$ref" : "#/definitions/AllowedAdditionalAnalyses"
        }
      },
      "additionalProperties" : False
    },
    "ConfiguredTableAssociationAnalysisRuleList" : {
      "type" : "object",
      "properties" : {
        "AllowedResultReceivers" : {
          "$ref" : "#/definitions/AllowedResultReceivers"
        },
        "AllowedAdditionalAnalyses" : {
          "$ref" : "#/definitions/AllowedAdditionalAnalyses"
        }
      },
      "additionalProperties" : False
    },
    "ConfiguredTableAssociationAnalysisRulePolicyV1" : {
      "oneOf" : [ {
        "type" : "object",
        "title" : "List",
        "properties" : {
          "List" : {
            "$ref" : "#/definitions/ConfiguredTableAssociationAnalysisRuleList"
          }
        },
        "required" : [ "List" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "title" : "Aggregation",
        "properties" : {
          "Aggregation" : {
            "$ref" : "#/definitions/ConfiguredTableAssociationAnalysisRuleAggregation"
          }
        },
        "required" : [ "Aggregation" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "title" : "Custom",
        "properties" : {
          "Custom" : {
            "$ref" : "#/definitions/ConfiguredTableAssociationAnalysisRuleCustom"
          }
        },
        "required" : [ "Custom" ],
        "additionalProperties" : False
      } ]
    },
    "ConfiguredTableAssociationAnalysisRulePolicy" : {
      "type" : "object",
      "title" : "V1",
      "properties" : {
        "V1" : {
          "$ref" : "#/definitions/ConfiguredTableAssociationAnalysisRulePolicyV1"
        }
      },
      "required" : [ "V1" ],
      "additionalProperties" : False
    },
    "ConfiguredTableAssociationAnalysisRule" : {
      "type" : "object",
      "properties" : {
        "Type" : {
          "$ref" : "#/definitions/ConfiguredTableAssociationAnalysisRuleType"
        },
        "Policy" : {
          "$ref" : "#/definitions/ConfiguredTableAssociationAnalysisRulePolicy"
        }
      },
      "required" : [ "Type", "Policy" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "maxLength" : 256
    },
    "Tags" : {
      "description" : "An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "type" : "array"
    },
    "ConfiguredTableAssociationIdentifier" : {
      "type" : "string",
      "maxLength" : 36,
      "minLength" : 36,
      "pattern" : "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    },
    "ConfiguredTableIdentifier" : {
      "type" : "string",
      "maxLength" : 36,
      "minLength" : 36,
      "pattern" : "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 255,
      "pattern" : "^[\\u0020-\\uD7FF\\uE000-\\uFFFD\\uD800\\uDBFF-\\uDC00\\uDFFF\\t\\r\\n]*$"
    },
    "MembershipIdentifier" : {
      "type" : "string",
      "maxLength" : 36,
      "minLength" : 36,
      "pattern" : "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 128,
      "pattern" : "^[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?$"
    },
    "RoleArn" : {
      "type" : "string",
      "maxLength" : 512,
      "minLength" : 32
    },
    "ConfiguredTableAssociationAnalysisRules" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/ConfiguredTableAssociationAnalysisRule"
      },
      "maxItems" : 1,
      "minItems" : 1
    }
  },
  "required" : [ "ConfiguredTableIdentifier", "Name", "RoleArn", "MembershipIdentifier" ],
  "readOnlyProperties" : [ "/properties/ConfiguredTableAssociationIdentifier", "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/ConfiguredTableIdentifier", "/properties/Name", "/properties/MembershipIdentifier" ],
  "primaryIdentifier" : [ "/properties/ConfiguredTableAssociationIdentifier", "/properties/MembershipIdentifier" ],
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
      "permissions" : [ "cleanrooms:CreateConfiguredTableAssociation", "iam:PassRole", "cleanrooms:ListTagsForResource", "cleanrooms:TagResource", "cleanrooms:GetConfiguredTableAssociation", "cleanrooms:ListConfiguredTableAssociations", "cleanrooms:DeleteConfiguredTableAssociation", "cleanrooms:DeleteConfiguredTableAssociationAnalysisRule", "cleanrooms:CreateConfiguredTableAssociationAnalysisRule", "cleanrooms:GetConfiguredTableAssociationAnalysisRule" ]
    },
    "read" : {
      "permissions" : [ "cleanrooms:GetConfiguredTableAssociation", "cleanrooms:ListTagsForResource", "cleanrooms:GetConfiguredTableAssociationAnalysisRule" ]
    },
    "update" : {
      "permissions" : [ "cleanrooms:UpdateConfiguredTableAssociation", "cleanrooms:GetConfiguredTableAssociation", "iam:PassRole", "cleanrooms:ListTagsForResource", "cleanrooms:TagResource", "cleanrooms:UntagResource", "cleanrooms:DeleteConfiguredTableAssociationAnalysisRule", "cleanrooms:CreateConfiguredTableAssociationAnalysisRule", "cleanrooms:GetConfiguredTableAssociationAnalysisRule", "cleanrooms:UpdateConfiguredTableAssociationAnalysisRule" ]
    },
    "delete" : {
      "permissions" : [ "cleanrooms:DeleteConfiguredTableAssociation", "cleanrooms:GetConfiguredTableAssociation", "cleanrooms:ListConfiguredTableAssociations", "cleanrooms:ListTagsForResource", "cleanrooms:UntagResource", "cleanrooms:DeleteConfiguredTableAssociationAnalysisRule", "cleanrooms:GetConfiguredTableAssociationAnalysisRule" ]
    },
    "list" : {
      "permissions" : [ "cleanrooms:ListConfiguredTableAssociations" ],
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