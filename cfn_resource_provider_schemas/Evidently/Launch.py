SCHEMA = {
  "typeName" : "AWS::Evidently::Launch",
  "description" : "Resource Type definition for AWS::Evidently::Launch.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-evidently",
  "properties" : {
    "Arn" : {
      "type" : "string",
      "pattern" : "arn:[^:]*:[^:]*:[^:]*:[^:]*:project/[-a-zA-Z0-9._]*/launch/[-a-zA-Z0-9._]*"
    },
    "Name" : {
      "type" : "string",
      "pattern" : "[-a-zA-Z0-9._]*",
      "minLength" : 1,
      "maxLength" : 127
    },
    "Project" : {
      "type" : "string",
      "pattern" : "([-a-zA-Z0-9._]*)|(arn:[^:]*:[^:]*:[^:]*:[^:]*:project/[-a-zA-Z0-9._]*)",
      "minLength" : 0,
      "maxLength" : 2048
    },
    "Description" : {
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 160
    },
    "RandomizationSalt" : {
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 127,
      "pattern" : ".*"
    },
    "ScheduledSplitsConfig" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/StepConfig"
      },
      "uniqueItems" : True,
      "insertionOrder" : True,
      "minItems" : 1,
      "maxItems" : 6
    },
    "Groups" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/LaunchGroupObject"
      },
      "uniqueItems" : True,
      "insertionOrder" : True,
      "minItems" : 1,
      "maxItems" : 5
    },
    "MetricMonitors" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/MetricDefinitionObject"
      },
      "uniqueItems" : True,
      "insertionOrder" : True,
      "minItems" : 0,
      "maxItems" : 3
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "ExecutionStatus" : {
      "description" : "Start or Stop Launch Launch. Default is not started.",
      "$ref" : "#/definitions/ExecutionStatusObject"
    }
  },
  "definitions" : {
    "ExecutionStatusObject" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Status" : {
          "description" : "Provide START or STOP action to apply on a launch",
          "type" : "string"
        },
        "DesiredState" : {
          "description" : "Provide CANCELLED or COMPLETED as the launch desired state. Defaults to Completed if not provided.",
          "type" : "string"
        },
        "Reason" : {
          "description" : "Provide a reason for stopping the launch. Defaults to empty if not provided.",
          "type" : "string"
        }
      },
      "required" : [ "Status" ]
    },
    "LaunchGroupObject" : {
      "type" : "object",
      "properties" : {
        "GroupName" : {
          "type" : "string",
          "pattern" : "[-a-zA-Z0-9._]*",
          "minLength" : 1,
          "maxLength" : 127
        },
        "Description" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 160
        },
        "Feature" : {
          "type" : "string"
        },
        "Variation" : {
          "type" : "string"
        }
      },
      "required" : [ "GroupName", "Feature", "Variation" ],
      "additionalProperties" : False
    },
    "GroupToWeight" : {
      "type" : "object",
      "properties" : {
        "GroupName" : {
          "type" : "string",
          "pattern" : "[-a-zA-Z0-9._]*",
          "minLength" : 1,
          "maxLength" : 127
        },
        "SplitWeight" : {
          "type" : "integer"
        }
      },
      "additionalProperties" : False,
      "required" : [ "GroupName", "SplitWeight" ]
    },
    "SegmentOverride" : {
      "type" : "object",
      "properties" : {
        "Segment" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 2048,
          "pattern" : "([-a-zA-Z0-9._]*)|(arn:[^:]*:[^:]*:[^:]*:[^:]*:segment/[-a-zA-Z0-9._]*)"
        },
        "EvaluationOrder" : {
          "type" : "integer"
        },
        "Weights" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/GroupToWeight"
          },
          "uniqueItems" : True,
          "insertionOrder" : False
        }
      },
      "additionalProperties" : False,
      "required" : [ "Segment", "EvaluationOrder", "Weights" ]
    },
    "StepConfig" : {
      "type" : "object",
      "properties" : {
        "StartTime" : {
          "type" : "string"
        },
        "GroupWeights" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/GroupToWeight"
          },
          "uniqueItems" : True,
          "insertionOrder" : False
        },
        "SegmentOverrides" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/SegmentOverride"
          },
          "uniqueItems" : True,
          "insertionOrder" : False
        }
      },
      "required" : [ "StartTime", "GroupWeights" ],
      "additionalProperties" : False
    },
    "MetricDefinitionObject" : {
      "type" : "object",
      "properties" : {
        "MetricName" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 255,
          "pattern" : "^[\\S]+$"
        },
        "EntityIdKey" : {
          "description" : "The JSON path to reference the entity id in the event.",
          "type" : "string"
        },
        "ValueKey" : {
          "description" : "The JSON path to reference the numerical metric value in the event.",
          "type" : "string"
        },
        "EventPattern" : {
          "description" : "Event patterns have the same structure as the events they match. Rules use event patterns to select events. An event pattern either matches an event or it doesn't.",
          "type" : "string"
        },
        "UnitLabel" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256,
          "pattern" : ".*"
        }
      },
      "required" : [ "MetricName", "EntityIdKey", "ValueKey" ],
      "additionalProperties" : False
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "pattern" : "^(?!aws:)[a-zA-Z+-=._:/]+$",
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
    }
  },
  "additionalProperties" : False,
  "required" : [ "Name", "Project", "Groups", "ScheduledSplitsConfig" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/Project" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "evidently:CreateLaunch", "evidently:TagResource", "evidently:GetLaunch", "evidently:StartLaunch" ]
    },
    "read" : {
      "permissions" : [ "evidently:GetLaunch", "evidently:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "evidently:UpdateLaunch", "evidently:ListTagsForResource", "evidently:TagResource", "evidently:UntagResource", "evidently:GetLaunch", "evidently:StartLaunch", "evidently:StopLaunch" ]
    },
    "delete" : {
      "permissions" : [ "evidently:DeleteLaunch", "evidently:UntagResource", "evidently:GetLaunch" ]
    }
  },
  "taggable" : True
}