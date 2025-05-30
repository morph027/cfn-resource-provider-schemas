SCHEMA = {
  "typeName" : "AWS::Glue::Job",
  "description" : "Resource Type definition for AWS::Glue::Job",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-glue.git",
  "definitions" : {
    "DefaultArguments" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      }
    },
    "NonOverridableArguments" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      }
    },
    "JobCommand" : {
      "type" : "object",
      "properties" : {
        "Name" : {
          "description" : "The name of the job command",
          "type" : "string"
        },
        "PythonVersion" : {
          "description" : "The Python version being used to execute a Python shell job.",
          "type" : "string"
        },
        "Runtime" : {
          "description" : "Runtime is used to specify the versions of Ray, Python and additional libraries available in your environment",
          "type" : "string"
        },
        "ScriptLocation" : {
          "description" : "Specifies the Amazon Simple Storage Service (Amazon S3) path to a script that executes a job",
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "ConnectionsList" : {
      "type" : "object",
      "properties" : {
        "Connections" : {
          "description" : "A list of connections used by the job.",
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        }
      },
      "additionalProperties" : False
    },
    "ExecutionProperty" : {
      "type" : "object",
      "properties" : {
        "MaxConcurrentRuns" : {
          "description" : "The maximum number of concurrent runs allowed for the job.",
          "type" : "number"
        }
      },
      "additionalProperties" : False
    },
    "NotificationProperty" : {
      "type" : "object",
      "properties" : {
        "NotifyDelayAfter" : {
          "description" : "It is the number of minutes to wait before sending a job run delay notification after a job run starts",
          "type" : "integer"
        }
      },
      "additionalProperties" : False
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "glue:TagResource", "glue:UntagResource" ]
  },
  "properties" : {
    "Connections" : {
      "$ref" : "#/definitions/ConnectionsList",
      "description" : "Specifies the connections used by a job"
    },
    "MaxRetries" : {
      "type" : "number",
      "description" : "The maximum number of times to retry this job after a JobRun fails"
    },
    "Description" : {
      "type" : "string",
      "description" : "A description of the job."
    },
    "Timeout" : {
      "type" : "integer",
      "description" : "The maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status."
    },
    "AllocatedCapacity" : {
      "type" : "number",
      "description" : "The number of capacity units that are allocated to this job."
    },
    "Name" : {
      "type" : "string",
      "description" : "The name you assign to the job definition"
    },
    "Role" : {
      "type" : "string",
      "description" : "The name or Amazon Resource Name (ARN) of the IAM role associated with this job."
    },
    "DefaultArguments" : {
      "type" : "object",
      "description" : "The default arguments for this job, specified as name-value pairs."
    },
    "NotificationProperty" : {
      "$ref" : "#/definitions/NotificationProperty",
      "description" : "Specifies configuration properties of a notification."
    },
    "WorkerType" : {
      "type" : "string",
      "description" : "TThe type of predefined worker that is allocated when a job runs.",
      "enum" : [ "Standard", "G.1X", "G.2X", "G.025X", "G.4X", "G.8X", "Z.2X" ]
    },
    "ExecutionClass" : {
      "type" : "string",
      "description" : "Indicates whether the job is run with a standard or flexible execution class."
    },
    "LogUri" : {
      "type" : "string",
      "description" : "This field is reserved for future use."
    },
    "Command" : {
      "$ref" : "#/definitions/JobCommand",
      "description" : "The code that executes a job."
    },
    "GlueVersion" : {
      "type" : "string",
      "description" : "Glue version determines the versions of Apache Spark and Python that AWS Glue supports."
    },
    "ExecutionProperty" : {
      "$ref" : "#/definitions/ExecutionProperty",
      "description" : "The maximum number of concurrent runs that are allowed for this job."
    },
    "SecurityConfiguration" : {
      "type" : "string",
      "description" : "The name of the SecurityConfiguration structure to be used with this job."
    },
    "NumberOfWorkers" : {
      "type" : "integer",
      "description" : "The number of workers of a defined workerType that are allocated when a job runs."
    },
    "Tags" : {
      "type" : "object",
      "description" : "The tags to use with this job."
    },
    "MaxCapacity" : {
      "type" : "number",
      "description" : "The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs."
    },
    "NonOverridableArguments" : {
      "type" : "object",
      "description" : "Non-overridable arguments for this job, specified as name-value pairs."
    },
    "MaintenanceWindow" : {
      "type" : "string",
      "description" : "Property description not available."
    },
    "JobMode" : {
      "type" : "string",
      "description" : "Property description not available."
    },
    "JobRunQueuingEnabled" : {
      "type" : "boolean",
      "description" : "Property description not available."
    }
  },
  "additionalProperties" : False,
  "required" : [ "Role", "Command" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:GetRole", "iam:PassRole", "glue:CreateJob", "glue:GetJob", "glue:TagResource" ]
    },
    "read" : {
      "permissions" : [ "glue:GetJob", "glue:GetTags" ]
    },
    "delete" : {
      "permissions" : [ "glue:DeleteJob", "glue:GetJob", "glue:UntagResource" ]
    },
    "update" : {
      "permissions" : [ "iam:GetRole", "iam:PassRole", "glue:UpdateJob", "glue:UntagResource", "glue:TagResource" ]
    },
    "list" : {
      "permissions" : [ "glue:ListJobs" ]
    }
  }
}