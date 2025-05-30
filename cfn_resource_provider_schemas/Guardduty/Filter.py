SCHEMA = {
  "typeName" : "AWS::GuardDuty::Filter",
  "description" : "Resource Type definition for AWS::GuardDuty::Filter",
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "guardduty:TagResource", "guardduty:UntagResource", "guardduty:ListTagsForResource" ]
  },
  "properties" : {
    "Action" : {
      "type" : "string"
    },
    "Description" : {
      "type" : "string"
    },
    "DetectorId" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 300
    },
    "FindingCriteria" : {
      "$ref" : "#/definitions/FindingCriteria"
    },
    "Rank" : {
      "type" : "integer",
      "minimum" : 1,
      "maximum" : 100
    },
    "Name" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 64
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/TagItem"
      }
    }
  },
  "definitions" : {
    "TagItem" : {
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
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ]
    },
    "Condition" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Lt" : {
          "type" : "integer"
        },
        "Gt" : {
          "type" : "integer"
        },
        "Gte" : {
          "type" : "integer"
        },
        "Neq" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "Eq" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "Lte" : {
          "type" : "integer"
        },
        "Equals" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "GreaterThan" : {
          "type" : "integer",
          "format" : "int64"
        },
        "GreaterThanOrEqual" : {
          "type" : "integer",
          "format" : "int64"
        },
        "LessThan" : {
          "type" : "integer",
          "format" : "int64"
        },
        "LessThanOrEqual" : {
          "type" : "integer",
          "format" : "int64"
        },
        "NotEquals" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        }
      }
    },
    "FindingCriteria" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Criterion" : {
          "type" : "object",
          "patternProperties" : {
            "^.+$" : {
              "$ref" : "#/definitions/Condition"
            }
          },
          "additionalProperties" : False
        }
      }
    }
  },
  "required" : [ "DetectorId", "Name", "FindingCriteria" ],
  "primaryIdentifier" : [ "/properties/DetectorId", "/properties/Name" ],
  "createOnlyProperties" : [ "/properties/DetectorId", "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "guardduty:CreateFilter", "guardduty:GetFilter", "guardduty:TagResource" ]
    },
    "read" : {
      "permissions" : [ "guardduty:GetFilter", "guardduty:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "guardduty:ListDetectors", "guardduty:ListFilters", "guardduty:GetFilter", "guardduty:DeleteFilter" ]
    },
    "update" : {
      "permissions" : [ "guardduty:UpdateFilter", "guardduty:GetFilter", "guardduty:ListFilters", "guardduty:TagResource", "guardduty:UntagResource" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "DetectorId" : {
            "type" : "string"
          }
        }
      },
      "permissions" : [ "guardduty:ListFilters" ]
    }
  }
}