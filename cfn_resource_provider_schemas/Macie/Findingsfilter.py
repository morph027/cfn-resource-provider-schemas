SCHEMA = {
  "typeName" : "AWS::Macie::FindingsFilter",
  "description" : "Macie FindingsFilter resource schema.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-macie.git",
  "definitions" : {
    "CriterionAdditionalProperties" : {
      "type" : "object",
      "properties" : {
        "gt" : {
          "type" : "integer",
          "format" : "int64"
        },
        "gte" : {
          "type" : "integer",
          "format" : "int64"
        },
        "lt" : {
          "type" : "integer",
          "format" : "int64"
        },
        "lte" : {
          "type" : "integer",
          "format" : "int64"
        },
        "eq" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        },
        "neq" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        }
      },
      "additionalProperties" : False
    },
    "Criterion" : {
      "description" : "Map of filter criteria.",
      "type" : "object",
      "patternProperties" : {
        "\\w" : {
          "$ref" : "#/definitions/CriterionAdditionalProperties"
        }
      },
      "additionalProperties" : False
    },
    "FindingCriteria" : {
      "type" : "object",
      "properties" : {
        "Criterion" : {
          "$ref" : "#/definitions/Criterion"
        }
      },
      "additionalProperties" : False
    },
    "FindingFilterAction" : {
      "type" : "string",
      "enum" : [ "ARCHIVE", "NOOP" ]
    },
    "FindingsFilterListItem" : {
      "description" : "Returned by ListHandler representing filter name and ID.",
      "type" : "object",
      "properties" : {
        "Id" : {
          "type" : "string"
        },
        "Name" : {
          "type" : "string"
        }
      }
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The tag's key."
        },
        "Value" : {
          "type" : "string",
          "description" : "The tag's value."
        }
      },
      "required" : [ "Value", "Key" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Name" : {
      "description" : "Findings filter name",
      "type" : "string"
    },
    "Description" : {
      "description" : "Findings filter description",
      "type" : "string"
    },
    "FindingCriteria" : {
      "description" : "Findings filter criteria.",
      "$ref" : "#/definitions/FindingCriteria"
    },
    "Action" : {
      "description" : "Findings filter action.",
      "$ref" : "#/definitions/FindingFilterAction"
    },
    "Position" : {
      "description" : "Findings filter position.",
      "type" : "integer"
    },
    "Id" : {
      "description" : "Findings filter ID.",
      "type" : "string"
    },
    "Arn" : {
      "description" : "Findings filter ARN.",
      "type" : "string"
    },
    "Tags" : {
      "description" : "A collection of tags associated with a resource",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "macie2:TagResource", "macie2:UntagResource" ]
  },
  "required" : [ "Name", "FindingCriteria" ],
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/Id", "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "additionalIdentifiers" : [ [ "/properties/Arn" ], [ "/properties/Name" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "macie2:GetFindingsFilter", "macie2:CreateFindingsFilter", "macie2:TagResource" ]
    },
    "read" : {
      "permissions" : [ "macie2:GetFindingsFilter" ]
    },
    "update" : {
      "permissions" : [ "macie2:GetFindingsFilter", "macie2:UpdateFindingsFilter", "macie2:TagResource", "macie2:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "macie2:DeleteFindingsFilter" ]
    },
    "list" : {
      "permissions" : [ "macie2:ListFindingsFilters" ]
    }
  }
}