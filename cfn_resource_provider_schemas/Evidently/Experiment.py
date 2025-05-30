SCHEMA = {
  "typeName" : "AWS::Evidently::Experiment",
  "description" : "Resource Type definition for AWS::Evidently::Experiment.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-evidently",
  "properties" : {
    "Arn" : {
      "type" : "string",
      "pattern" : "arn:[^:]*:[^:]*:[^:]*:[^:]*:project/[-a-zA-Z0-9._]*/experiment/[-a-zA-Z0-9._]*"
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
    "RunningStatus" : {
      "description" : "Start Experiment. Default is False",
      "$ref" : "#/definitions/RunningStatusObject"
    },
    "RandomizationSalt" : {
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 127,
      "pattern" : ".*"
    },
    "Treatments" : {
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : True,
      "items" : {
        "$ref" : "#/definitions/TreatmentObject"
      },
      "minItems" : 2,
      "maxItems" : 5
    },
    "MetricGoals" : {
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : True,
      "items" : {
        "$ref" : "#/definitions/MetricGoalObject"
      },
      "minItems" : 1,
      "maxItems" : 3
    },
    "SamplingRate" : {
      "type" : "integer",
      "minimum" : 0,
      "maximum" : 100000
    },
    "OnlineAbConfig" : {
      "$ref" : "#/definitions/OnlineAbConfigObject"
    },
    "Segment" : {
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 2048,
      "pattern" : "([-a-zA-Z0-9._]*)|(arn:[^:]*:[^:]*:[^:]*:[^:]*:segment/[-a-zA-Z0-9._]*)"
    },
    "RemoveSegment" : {
      "type" : "boolean"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "definitions" : {
    "RunningStatusObject" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Status" : {
          "description" : "Provide START or STOP action to apply on an experiment",
          "type" : "string"
        },
        "AnalysisCompleteTime" : {
          "description" : "Provide the analysis Completion time for an experiment",
          "type" : "string"
        },
        "Reason" : {
          "description" : "Reason is a required input for stopping the experiment",
          "type" : "string"
        },
        "DesiredState" : {
          "description" : "Provide CANCELLED or COMPLETED desired state when stopping an experiment",
          "type" : "string",
          "pattern" : "^(CANCELLED|COMPLETED)"
        }
      },
      "oneOf" : [ {
        "required" : [ "Status", "AnalysisCompleteTime" ]
      }, {
        "required" : [ "Status", "Reason", "DesiredState" ]
      } ]
    },
    "TreatmentObject" : {
      "type" : "object",
      "properties" : {
        "TreatmentName" : {
          "type" : "string",
          "pattern" : "[-a-zA-Z0-9._]*",
          "minLength" : 1,
          "maxLength" : 127
        },
        "Description" : {
          "type" : "string"
        },
        "Feature" : {
          "type" : "string",
          "pattern" : "([-a-zA-Z0-9._]*)|(arn:[^:]*:[^:]*:[^:]*:[^:]*:.*)"
        },
        "Variation" : {
          "type" : "string",
          "pattern" : "[-a-zA-Z0-9._]*",
          "minLength" : 1,
          "maxLength" : 255
        }
      },
      "required" : [ "TreatmentName", "Feature", "Variation" ],
      "additionalProperties" : False
    },
    "MetricGoalObject" : {
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
        },
        "DesiredChange" : {
          "type" : "string",
          "enum" : [ "INCREASE", "DECREASE" ]
        }
      },
      "required" : [ "MetricName", "EntityIdKey", "ValueKey", "DesiredChange" ],
      "additionalProperties" : False
    },
    "OnlineAbConfigObject" : {
      "type" : "object",
      "properties" : {
        "ControlTreatmentName" : {
          "type" : "string",
          "pattern" : "[-a-zA-Z0-9._]*",
          "minLength" : 1,
          "maxLength" : 127
        },
        "TreatmentWeights" : {
          "type" : "array",
          "uniqueItems" : True,
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/TreatmentToWeight"
          }
        }
      },
      "additionalProperties" : False
    },
    "TreatmentToWeight" : {
      "type" : "object",
      "properties" : {
        "Treatment" : {
          "type" : "string",
          "pattern" : "[-a-zA-Z0-9._]*",
          "minLength" : 1,
          "maxLength" : 127
        },
        "SplitWeight" : {
          "type" : "integer",
          "minimum" : 0,
          "maximum" : 100000
        }
      },
      "required" : [ "Treatment", "SplitWeight" ],
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
  "required" : [ "Name", "Project", "Treatments", "MetricGoals", "OnlineAbConfig" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/Project" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "evidently:CreateExperiment", "evidently:TagResource", "evidently:GetExperiment", "evidently:StartExperiment" ]
    },
    "read" : {
      "permissions" : [ "evidently:GetExperiment", "evidently:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "evidently:UpdateExperiment", "evidently:TagResource", "evidently:UntagResource", "evidently:GetExperiment", "evidently:StartExperiment", "evidently:StopExperiment" ]
    },
    "delete" : {
      "permissions" : [ "evidently:DeleteExperiment", "evidently:UntagResource", "evidently:GetExperiment" ]
    }
  },
  "taggable" : True
}