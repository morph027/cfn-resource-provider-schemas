SCHEMA = {
  "typeName" : "AWS::CustomerProfiles::CalculatedAttributeDefinition",
  "description" : "A calculated attribute definition for Customer Profiles",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-customer-profiles",
  "definitions" : {
    "DomainName" : {
      "description" : "The unique name of the domain.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9_-]+$",
      "minLength" : 1,
      "maxLength" : 64
    },
    "CalculatedAttributeName" : {
      "description" : "The unique name of the calculated attribute.",
      "type" : "string",
      "pattern" : "^[a-zA-Z_][a-zA-Z_0-9-]*$",
      "minLength" : 1,
      "maxLength" : 255
    },
    "DisplayName" : {
      "description" : "The display name of the calculated attribute.",
      "type" : "string",
      "pattern" : "^[a-zA-Z_][a-zA-Z_0-9-\\s]*$",
      "minLength" : 1,
      "maxLength" : 255
    },
    "Description" : {
      "description" : "The description of the calculated attribute.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 1000
    },
    "AttributeName" : {
      "description" : "The name of an attribute defined in a profile object type.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9_.-]+$",
      "minLength" : 1,
      "maxLength" : 64
    },
    "AttributeItem" : {
      "description" : "The details of a single attribute item specified in the mathematical expression.",
      "type" : "object",
      "properties" : {
        "Name" : {
          "$ref" : "#/definitions/AttributeName"
        }
      },
      "required" : [ "Name" ],
      "additionalProperties" : False
    },
    "AttributeList" : {
      "description" : "A list of attribute items specified in the mathematical expression.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/AttributeItem"
      },
      "insertionOrder" : False,
      "uniqueItems" : True,
      "minItems" : 1,
      "maxItems" : 2
    },
    "Expression" : {
      "description" : "Mathematical expression that is performed on attribute items provided in the attribute list. Each element in the expression should follow the structure of \"{ObjectTypeName.AttributeName}\".",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "AttributeDetails" : {
      "description" : "Mathematical expression and a list of attribute items specified in that expression.",
      "type" : "object",
      "properties" : {
        "Attributes" : {
          "$ref" : "#/definitions/AttributeList"
        },
        "Expression" : {
          "$ref" : "#/definitions/Expression"
        }
      },
      "required" : [ "Attributes", "Expression" ],
      "additionalProperties" : False
    },
    "RangeUnit" : {
      "description" : "The unit of time.",
      "type" : "string",
      "enum" : [ "DAYS" ]
    },
    "RangeValue" : {
      "description" : "The amount of time of the specified unit.",
      "type" : "integer",
      "minimum" : 1,
      "maximum" : 366
    },
    "Range" : {
      "description" : "The relative time period over which data is included in the aggregation.",
      "type" : "object",
      "properties" : {
        "Value" : {
          "$ref" : "#/definitions/RangeValue"
        },
        "Unit" : {
          "$ref" : "#/definitions/RangeUnit"
        }
      },
      "required" : [ "Value", "Unit" ],
      "additionalProperties" : False
    },
    "ObjectCount" : {
      "description" : "The number of profile objects used for the calculated attribute.",
      "type" : "integer",
      "minimum" : 1,
      "maximum" : 100
    },
    "ThresholdValue" : {
      "description" : "The value of the threshold.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "ThresholdOperator" : {
      "description" : "The operator of the threshold.",
      "type" : "string",
      "enum" : [ "EQUAL_TO", "GREATER_THAN", "LESS_THAN", "NOT_EQUAL_TO" ]
    },
    "Threshold" : {
      "description" : "The threshold for the calculated attribute.",
      "type" : "object",
      "properties" : {
        "Value" : {
          "$ref" : "#/definitions/ThresholdValue"
        },
        "Operator" : {
          "$ref" : "#/definitions/ThresholdOperator"
        }
      },
      "required" : [ "Value", "Operator" ],
      "additionalProperties" : False
    },
    "Conditions" : {
      "description" : "The conditions including range, object count, and threshold for the calculated attribute.",
      "type" : "object",
      "properties" : {
        "Range" : {
          "$ref" : "#/definitions/Range"
        },
        "ObjectCount" : {
          "$ref" : "#/definitions/ObjectCount"
        },
        "Threshold" : {
          "$ref" : "#/definitions/Threshold"
        }
      },
      "additionalProperties" : False
    },
    "Statistic" : {
      "description" : "The aggregation operation to perform for the calculated attribute.",
      "type" : "string",
      "enum" : [ "FIRST_OCCURRENCE", "LAST_OCCURRENCE", "COUNT", "SUM", "MINIMUM", "MAXIMUM", "AVERAGE", "MAX_OCCURRENCE" ]
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "minItems" : 0,
      "maxItems" : 50
    }
  },
  "properties" : {
    "DomainName" : {
      "$ref" : "#/definitions/DomainName"
    },
    "CalculatedAttributeName" : {
      "$ref" : "#/definitions/CalculatedAttributeName"
    },
    "DisplayName" : {
      "$ref" : "#/definitions/DisplayName"
    },
    "Description" : {
      "$ref" : "#/definitions/Description"
    },
    "AttributeDetails" : {
      "$ref" : "#/definitions/AttributeDetails"
    },
    "Conditions" : {
      "$ref" : "#/definitions/Conditions"
    },
    "Statistic" : {
      "$ref" : "#/definitions/Statistic"
    },
    "CreatedAt" : {
      "description" : "The timestamp of when the calculated attribute definition was created.",
      "type" : "string"
    },
    "LastUpdatedAt" : {
      "description" : "The timestamp of when the calculated attribute definition was most recently edited.",
      "type" : "string"
    },
    "Tags" : {
      "$ref" : "#/definitions/Tags"
    }
  },
  "additionalProperties" : False,
  "required" : [ "DomainName", "CalculatedAttributeName", "AttributeDetails", "Statistic" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "profile:TagResource", "profile:UntagResource", "profile:ListTagsForResource" ]
  },
  "createOnlyProperties" : [ "/properties/DomainName", "/properties/CalculatedAttributeName" ],
  "readOnlyProperties" : [ "/properties/CreatedAt", "/properties/LastUpdatedAt" ],
  "primaryIdentifier" : [ "/properties/DomainName", "/properties/CalculatedAttributeName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "profile:CreateCalculatedAttributeDefinition", "profile:TagResource" ]
    },
    "read" : {
      "permissions" : [ "profile:GetCalculatedAttributeDefinition" ]
    },
    "update" : {
      "permissions" : [ "profile:GetCalculatedAttributeDefinition", "profile:UpdateCalculatedAttributeDefinition", "profile:UntagResource", "profile:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "profile:DeleteCalculatedAttributeDefinition" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "DomainName" : {
            "$ref" : "resource-schema.json#/properties/DomainName"
          }
        },
        "required" : [ "DomainName" ]
      },
      "permissions" : [ "profile:ListCalculatedAttributeDefinitions" ]
    }
  }
}