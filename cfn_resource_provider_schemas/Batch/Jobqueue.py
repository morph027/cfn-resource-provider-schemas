SCHEMA = {
  "typeName" : "AWS::Batch::JobQueue",
  "description" : "Resource Type definition for AWS::Batch::JobQueue",
  "additionalProperties" : False,
  "definitions" : {
    "ResourceArn" : {
      "type" : "string",
      "pattern" : "arn:[a-z0-9-\\.]{1,63}:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[^/].{0,1023}"
    },
    "ComputeEnvironmentOrder" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ComputeEnvironment" : {
          "type" : "string"
        },
        "Order" : {
          "type" : "integer"
        }
      },
      "required" : [ "ComputeEnvironment", "Order" ]
    },
    "JobStateTimeLimitAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Action" : {
          "type" : "string",
          "enum" : [ "CANCEL" ]
        },
        "MaxTimeSeconds" : {
          "type" : "integer",
          "minimum" : 600,
          "maximum" : 86400
        },
        "Reason" : {
          "type" : "string"
        },
        "State" : {
          "type" : "string",
          "enum" : [ "RUNNABLE" ]
        }
      },
      "required" : [ "Action", "MaxTimeSeconds", "Reason", "State" ]
    }
  },
  "properties" : {
    "JobQueueName" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128
    },
    "JobQueueArn" : {
      "$ref" : "#/definitions/ResourceArn"
    },
    "ComputeEnvironmentOrder" : {
      "type" : "array",
      "insertionOrder" : True,
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/ComputeEnvironmentOrder"
      }
    },
    "JobStateTimeLimitActions" : {
      "type" : "array",
      "insertionOrder" : True,
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/JobStateTimeLimitAction"
      }
    },
    "Priority" : {
      "type" : "integer",
      "minimum" : 0,
      "maximum" : 1000
    },
    "State" : {
      "type" : "string",
      "enum" : [ "DISABLED", "ENABLED" ]
    },
    "SchedulingPolicyArn" : {
      "$ref" : "#/definitions/ResourceArn"
    },
    "Tags" : {
      "type" : "object",
      "description" : "A key-value pair to associate with a resource.",
      "patternProperties" : {
        ".*" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "Batch:TagResource", "Batch:UntagResource" ]
  },
  "required" : [ "ComputeEnvironmentOrder", "Priority" ],
  "primaryIdentifier" : [ "/properties/JobQueueArn" ],
  "createOnlyProperties" : [ "/properties/Tags", "/properties/JobQueueName" ],
  "readOnlyProperties" : [ "/properties/JobQueueArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "Batch:CreateJobQueue", "Batch:TagResource", "Batch:DescribeJobQueues" ]
    },
    "read" : {
      "permissions" : [ "Batch:DescribeJobQueues" ]
    },
    "update" : {
      "permissions" : [ "Batch:DescribeJobQueues", "Batch:UpdateJobQueue", "Batch:TagResource", "Batch:UnTagResource" ]
    },
    "delete" : {
      "permissions" : [ "Batch:UpdateJobQueue", "Batch:DescribeJobQueues", "Batch:DeleteJobQueue" ]
    },
    "list" : {
      "permissions" : [ "Batch:DescribeJobQueues" ]
    }
  }
}