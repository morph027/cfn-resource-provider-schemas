SCHEMA = {
  "typeName" : "AWS::CustomerProfiles::EventTrigger",
  "description" : "An event trigger resource of Amazon Connect Customer Profiles",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-customer-profiles",
  "definitions" : {
    "DomainName" : {
      "description" : "The unique name of the domain.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9_-]+$",
      "minLength" : 1,
      "maxLength" : 64
    },
    "EventTriggerName" : {
      "description" : "The unique name of the event trigger.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9_-]+$",
      "minLength" : 1,
      "maxLength" : 64
    },
    "ObjectTypeName" : {
      "description" : "The unique name of the object type.",
      "type" : "string",
      "pattern" : "^[a-zA-Z_][a-zA-Z_0-9-]*$",
      "minLength" : 1,
      "maxLength" : 255
    },
    "Description" : {
      "description" : "The description of the event trigger.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 1000
    },
    "EventTriggerConditions" : {
      "description" : "A list of conditions that determine when an event should trigger the destination.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/EventTriggerCondition"
      },
      "insertionOrder" : False,
      "minItems" : 1,
      "maxItems" : 5
    },
    "EventTriggerCondition" : {
      "description" : "Specifies the circumstances under which the event should trigger the destination.",
      "type" : "object",
      "properties" : {
        "EventTriggerDimensions" : {
          "$ref" : "#/definitions/EventTriggerDimensions"
        },
        "LogicalOperator" : {
          "$ref" : "#/definitions/EventTriggerLogicalOperator"
        }
      },
      "required" : [ "EventTriggerDimensions", "LogicalOperator" ],
      "additionalProperties" : False
    },
    "EventTriggerDimensions" : {
      "description" : "A list of dimensions to be evaluated for the event.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/EventTriggerDimension"
      },
      "insertionOrder" : False,
      "minItems" : 1,
      "maxItems" : 10
    },
    "EventTriggerDimension" : {
      "description" : "A specific event dimension to be assessed.",
      "type" : "object",
      "properties" : {
        "ObjectAttributes" : {
          "$ref" : "#/definitions/ObjectAttributes"
        }
      },
      "required" : [ "ObjectAttributes" ],
      "additionalProperties" : False
    },
    "EventTriggerLogicalOperator" : {
      "description" : "The operator used to combine multiple dimensions.",
      "type" : "string",
      "enum" : [ "ANY", "ALL", "NONE" ]
    },
    "ObjectAttributes" : {
      "description" : "A list of object attributes to be evaluated.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/ObjectAttribute"
      },
      "insertionOrder" : False,
      "minItems" : 1,
      "maxItems" : 10
    },
    "ObjectAttribute" : {
      "description" : "The criteria that a specific object attribute must meet to trigger the destination.",
      "type" : "object",
      "properties" : {
        "Source" : {
          "description" : "An attribute contained within a source object.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 1000
        },
        "FieldName" : {
          "description" : "A field defined within an object type.",
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9_.-]+$",
          "minLength" : 1,
          "maxLength" : 64
        },
        "ComparisonOperator" : {
          "description" : "The operator used to compare an attribute against a list of values.",
          "type" : "string",
          "enum" : [ "INCLUSIVE", "EXCLUSIVE", "CONTAINS", "BEGINS_WITH", "ENDS_WITH", "GREATER_THAN", "LESS_THAN", "GREATER_THAN_OR_EQUAL", "LESS_THAN_OR_EQUAL", "EQUAL", "BEFORE", "AFTER", "ON", "BETWEEN", "NOT_BETWEEN" ]
        },
        "Values" : {
          "description" : "A list of attribute values used for comparison.",
          "type" : "array",
          "items" : {
            "type" : "string",
            "minLength" : 1,
            "maxLength" : 255
          },
          "insertionOrder" : False,
          "minItems" : 1,
          "maxItems" : 10
        }
      },
      "required" : [ "ComparisonOperator", "Values" ],
      "additionalProperties" : False
    },
    "EventTriggerLimits" : {
      "description" : "Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.",
      "type" : "object",
      "properties" : {
        "EventExpiration" : {
          "$ref" : "#/definitions/EventExpiration"
        },
        "Periods" : {
          "$ref" : "#/definitions/Periods"
        }
      },
      "additionalProperties" : False
    },
    "EventExpiration" : {
      "description" : "Specifies that an event will only trigger the destination if it is processed within a certain latency period.",
      "type" : "integer",
      "format" : "int64"
    },
    "Periods" : {
      "description" : "A list of time periods during which the limits apply.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Period"
      },
      "insertionOrder" : False,
      "minItems" : 1,
      "maxItems" : 4
    },
    "Period" : {
      "description" : "Defines a limit and the time period during which it is enforced.",
      "type" : "object",
      "properties" : {
        "Unit" : {
          "description" : "The unit of time.",
          "type" : "string",
          "enum" : [ "HOURS", "DAYS", "WEEKS", "MONTHS" ]
        },
        "Value" : {
          "description" : "The amount of time of the specified unit.",
          "type" : "integer",
          "minimum" : 1,
          "maximum" : 24
        },
        "MaxInvocationsPerProfile" : {
          "description" : "The maximum allowed number of destination invocations per profile.",
          "type" : "integer",
          "minimum" : 1,
          "maximum" : 1000
        },
        "Unlimited" : {
          "description" : "If set to True, there is no limit on the number of destination invocations per profile. The default is False.",
          "type" : "boolean"
        }
      },
      "required" : [ "Unit", "Value" ],
      "additionalProperties" : False
    },
    "SegmentFilter" : {
      "description" : "The destination is triggered only for profiles that meet the criteria of a segment definition.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9_-]+$",
      "minLength" : 1,
      "maxLength" : 64
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
    "EventTriggerName" : {
      "$ref" : "#/definitions/EventTriggerName"
    },
    "ObjectTypeName" : {
      "$ref" : "#/definitions/ObjectTypeName"
    },
    "Description" : {
      "$ref" : "#/definitions/Description"
    },
    "EventTriggerConditions" : {
      "$ref" : "#/definitions/EventTriggerConditions"
    },
    "EventTriggerLimits" : {
      "$ref" : "#/definitions/EventTriggerLimits"
    },
    "SegmentFilter" : {
      "$ref" : "#/definitions/SegmentFilter"
    },
    "CreatedAt" : {
      "description" : "The timestamp of when the event trigger was created.",
      "type" : "string"
    },
    "LastUpdatedAt" : {
      "description" : "The timestamp of when the event trigger was most recently updated.",
      "type" : "string"
    },
    "Tags" : {
      "$ref" : "#/definitions/Tags"
    }
  },
  "additionalProperties" : False,
  "required" : [ "DomainName", "EventTriggerName", "ObjectTypeName", "EventTriggerConditions" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "profile:TagResource", "profile:UntagResource", "profile:ListTagsForResource" ]
  },
  "createOnlyProperties" : [ "/properties/DomainName", "/properties/EventTriggerName" ],
  "readOnlyProperties" : [ "/properties/CreatedAt", "/properties/LastUpdatedAt" ],
  "primaryIdentifier" : [ "/properties/DomainName", "/properties/EventTriggerName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "profile:CreateEventTrigger", "profile:TagResource" ]
    },
    "read" : {
      "permissions" : [ "profile:GetEventTrigger" ]
    },
    "update" : {
      "permissions" : [ "profile:GetEventTrigger", "profile:UpdateEventTrigger", "profile:UntagResource", "profile:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "profile:DeleteEventTrigger" ]
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
      "permissions" : [ "profile:ListEventTriggers" ]
    }
  }
}