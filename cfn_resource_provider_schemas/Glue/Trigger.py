SCHEMA = {
  "typeName" : "AWS::Glue::Trigger",
  "description" : "Resource Type definition for AWS::Glue::Trigger",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-glue.git",
  "additionalProperties" : False,
  "properties" : {
    "Type" : {
      "type" : "string",
      "description" : "The type of trigger that this is."
    },
    "StartOnCreation" : {
      "type" : "boolean",
      "description" : "Set to True to start SCHEDULED and CONDITIONAL triggers when created. True is not supported for ON_DEMAND triggers."
    },
    "Description" : {
      "type" : "string",
      "description" : "A description of this trigger."
    },
    "Actions" : {
      "type" : "array",
      "description" : "The actions initiated by this trigger.",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Action"
      }
    },
    "EventBatchingCondition" : {
      "$ref" : "#/definitions/EventBatchingCondition",
      "description" : "Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires."
    },
    "WorkflowName" : {
      "type" : "string",
      "description" : "The name of the workflow associated with the trigger."
    },
    "Schedule" : {
      "type" : "string",
      "description" : "A cron expression used to specify the schedule."
    },
    "Tags" : {
      "type" : "object",
      "description" : "The tags to use with this trigger."
    },
    "Name" : {
      "type" : "string",
      "description" : "The name of the trigger."
    },
    "Predicate" : {
      "$ref" : "#/definitions/Predicate",
      "description" : "The predicate of this trigger, which defines when it will fire."
    }
  },
  "definitions" : {
    "Condition" : {
      "type" : "object",
      "description" : "Defines a condition under which a trigger fires.",
      "additionalProperties" : False,
      "properties" : {
        "JobName" : {
          "type" : "string",
          "description" : "The name of the job whose JobRuns this condition applies to, and on which this trigger waits."
        },
        "CrawlerName" : {
          "type" : "string",
          "description" : "The name of the crawler to which this condition applies."
        },
        "State" : {
          "type" : "string",
          "description" : "The condition state. Currently, the values supported are SUCCEEDED, STOPPED, TIMEOUT, and FAILED."
        },
        "CrawlState" : {
          "type" : "string",
          "description" : "The state of the crawler to which this condition applies."
        },
        "LogicalOperator" : {
          "type" : "string",
          "description" : "A logical operator."
        }
      }
    },
    "NotificationProperty" : {
      "type" : "object",
      "description" : "Specifies configuration properties of a job run notification.",
      "additionalProperties" : False,
      "properties" : {
        "NotifyDelayAfter" : {
          "type" : "integer",
          "description" : "After a job run starts, the number of minutes to wait before sending a job run delay notification"
        }
      }
    },
    "Action" : {
      "type" : "object",
      "description" : "The actions initiated by this trigger.",
      "additionalProperties" : False,
      "properties" : {
        "NotificationProperty" : {
          "$ref" : "#/definitions/NotificationProperty",
          "description" : "Specifies configuration properties of a job run notification."
        },
        "CrawlerName" : {
          "type" : "string",
          "description" : "The name of the crawler to be used with this action."
        },
        "Timeout" : {
          "type" : "integer",
          "description" : "The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job."
        },
        "JobName" : {
          "type" : "string",
          "description" : "The name of a job to be executed."
        },
        "Arguments" : {
          "type" : "object",
          "description" : "The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself."
        },
        "SecurityConfiguration" : {
          "type" : "string",
          "description" : "The name of the SecurityConfiguration structure to be used with this action."
        }
      }
    },
    "EventBatchingCondition" : {
      "type" : "object",
      "description" : "Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.",
      "additionalProperties" : False,
      "properties" : {
        "BatchSize" : {
          "type" : "integer",
          "description" : "Number of events that must be received from Amazon EventBridge before EventBridge event trigger fires."
        },
        "BatchWindow" : {
          "type" : "integer",
          "description" : "Window of time in seconds after which EventBridge event trigger fires. Window starts when first event is received."
        }
      },
      "required" : [ "BatchSize" ]
    },
    "Predicate" : {
      "type" : "object",
      "description" : "The predicate of this trigger, which defines when it will fire.",
      "additionalProperties" : False,
      "properties" : {
        "Logical" : {
          "type" : "string",
          "description" : "An optional field if only one condition is listed. If multiple conditions are listed, then this field is required."
        },
        "Conditions" : {
          "type" : "array",
          "description" : "A list of the conditions that determine when the trigger will fire.",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/Condition"
          }
        }
      }
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
  "required" : [ "Type", "Actions" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/WorkflowName", "/properties/Type" ],
  "writeOnlyProperties" : [ "/properties/StartOnCreation" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "glue:CreateTrigger", "glue:GetTrigger", "glue:TagResource" ]
    },
    "read" : {
      "permissions" : [ "glue:GetTrigger", "glue:GetTags" ]
    },
    "update" : {
      "permissions" : [ "glue:UpdateTrigger", "glue:UntagResource", "glue:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "glue:DeleteTrigger", "glue:GetTrigger" ]
    },
    "list" : {
      "permissions" : [ "glue:ListTriggers" ]
    }
  }
}