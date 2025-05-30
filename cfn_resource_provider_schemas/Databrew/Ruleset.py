SCHEMA = {
  "typeName" : "AWS::DataBrew::Ruleset",
  "description" : "Resource schema for AWS::DataBrew::Ruleset.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-databrew.git",
  "definitions" : {
    "Expression" : {
      "description" : "Expression with rule conditions",
      "type" : "string",
      "minLength" : 4,
      "maxLength" : 1024,
      "pattern" : "^[><0-9A-Za-z_.,:)(!= ]+$"
    },
    "SubstitutionValue" : {
      "description" : "A key-value pair to associate expression's substitution variable names with their values",
      "type" : "object",
      "properties" : {
        "ValueReference" : {
          "description" : "Variable name",
          "type" : "string",
          "minLength" : 2,
          "maxLength" : 128,
          "pattern" : "^:[A-Za-z0-9_]+$"
        },
        "Value" : {
          "description" : "Value or column name",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 1024
        }
      },
      "additionalProperties" : False,
      "required" : [ "ValueReference", "Value" ]
    },
    "ValuesMap" : {
      "type" : "array",
      "insertionOrder" : True,
      "items" : {
        "$ref" : "#/definitions/SubstitutionValue"
      }
    },
    "ThresholdValue" : {
      "description" : "Threshold value for a rule",
      "type" : "number"
    },
    "ThresholdType" : {
      "description" : "Threshold type for a rule",
      "enum" : [ "GREATER_THAN_OR_EQUAL", "LESS_THAN_OR_EQUAL", "GREATER_THAN", "LESS_THAN" ],
      "type" : "string"
    },
    "ThresholdUnit" : {
      "description" : "Threshold unit for a rule",
      "enum" : [ "COUNT", "PERCENTAGE" ],
      "type" : "string"
    },
    "Threshold" : {
      "type" : "object",
      "properties" : {
        "Value" : {
          "$ref" : "#/definitions/ThresholdValue"
        },
        "Type" : {
          "$ref" : "#/definitions/ThresholdType"
        },
        "Unit" : {
          "$ref" : "#/definitions/ThresholdUnit"
        }
      },
      "required" : [ "Value" ],
      "additionalProperties" : False
    },
    "ColumnSelector" : {
      "description" : "Selector of a column from a dataset for profile job configuration. One selector includes either a column name or a regular expression",
      "type" : "object",
      "properties" : {
        "Regex" : {
          "description" : "A regular expression for selecting a column from a dataset",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 255
        },
        "Name" : {
          "description" : "The name of a column from a dataset",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 255
        }
      },
      "additionalProperties" : False
    },
    "Disabled" : {
      "description" : "Boolean value to disable/enable a rule",
      "type" : "boolean"
    },
    "Rule" : {
      "description" : "Data quality rule for a target resource (dataset)",
      "type" : "object",
      "properties" : {
        "Name" : {
          "description" : "Name of the rule",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Disabled" : {
          "$ref" : "#/definitions/Disabled"
        },
        "CheckExpression" : {
          "$ref" : "#/definitions/Expression"
        },
        "SubstitutionMap" : {
          "$ref" : "#/definitions/ValuesMap"
        },
        "Threshold" : {
          "$ref" : "#/definitions/Threshold"
        },
        "ColumnSelectors" : {
          "type" : "array",
          "insertionOrder" : True,
          "items" : {
            "$ref" : "#/definitions/ColumnSelector"
          },
          "minItems" : 1
        }
      },
      "required" : [ "Name", "CheckExpression" ],
      "additionalProperties" : False
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "additionalProperties" : False,
      "required" : [ "Value", "Key" ]
    }
  },
  "properties" : {
    "Name" : {
      "description" : "Name of the Ruleset",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "Description" : {
      "description" : "Description of the Ruleset",
      "type" : "string",
      "maxLength" : 1024
    },
    "TargetArn" : {
      "description" : "Arn of the target resource (dataset) to apply the ruleset to",
      "type" : "string",
      "minLength" : 20,
      "maxLength" : 2048
    },
    "Rules" : {
      "description" : "List of the data quality rules in the ruleset",
      "type" : "array",
      "insertionOrder" : True,
      "items" : {
        "$ref" : "#/definitions/Rule"
      },
      "minItems" : 1
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "required" : [ "Name", "TargetArn", "Rules" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/TargetArn" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "databrew:TagResource", "databrew:UntagResource", "databrew:ListTagsForResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "databrew:CreateRuleset", "databrew:DescribeRuleset", "databrew:TagResource", "databrew:UntagResource", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "databrew:DescribeRuleset", "iam:ListRoles" ]
    },
    "update" : {
      "permissions" : [ "databrew:UpdateRuleset", "databrew:TagResource", "databrew:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "databrew:DeleteRuleset" ]
    },
    "list" : {
      "permissions" : [ "databrew:ListRulesets", "databrew:ListTagsForResource", "iam:ListRoles" ]
    }
  }
}