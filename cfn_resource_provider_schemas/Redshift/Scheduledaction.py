SCHEMA = {
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-redshift",
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "read" : {
      "permissions" : [ "redshift:DescribeScheduledActions", "redshift:DescribeTags" ]
    },
    "create" : {
      "permissions" : [ "redshift:CreateScheduledAction", "redshift:DescribeScheduledActions", "redshift:DescribeTags", "redshift:PauseCluster", "redshift:ResumeCluster", "redshift:ResizeCluster", "iam:PassRole" ]
    },
    "update" : {
      "permissions" : [ "redshift:DescribeScheduledActions", "redshift:ModifyScheduledAction", "redshift:PauseCluster", "redshift:ResumeCluster", "redshift:ResizeCluster", "redshift:DescribeTags", "iam:PassRole" ]
    },
    "list" : {
      "permissions" : [ "redshift:DescribeTags", "redshift:DescribeScheduledActions" ]
    },
    "delete" : {
      "permissions" : [ "redshift:DescribeTags", "redshift:DescribeScheduledActions", "redshift:DeleteScheduledAction" ]
    }
  },
  "typeName" : "AWS::Redshift::ScheduledAction",
  "readOnlyProperties" : [ "/properties/State", "/properties/NextInvocations" ],
  "description" : "The `AWS::Redshift::ScheduledAction` resource creates an Amazon Redshift Scheduled Action.",
  "createOnlyProperties" : [ "/properties/ScheduledActionName" ],
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/ScheduledActionName" ],
  "definitions" : {
    "ScheduledActionType" : {
      "oneOf" : [ {
        "additionalProperties" : False,
        "properties" : {
          "ResizeCluster" : {
            "$ref" : "#/definitions/ResizeClusterMessage"
          }
        }
      }, {
        "additionalProperties" : False,
        "properties" : {
          "PauseCluster" : {
            "$ref" : "#/definitions/PauseClusterMessage"
          }
        }
      }, {
        "additionalProperties" : False,
        "properties" : {
          "ResumeCluster" : {
            "$ref" : "#/definitions/ResumeClusterMessage"
          }
        }
      } ],
      "type" : "object"
    },
    "ResizeClusterMessage" : {
      "description" : "Describes a resize cluster operation. For example, a scheduled action to run the `ResizeCluster` API operation.",
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "NodeType" : {
          "relationshipRef" : {
            "typeName" : "AWS::Redshift::Cluster",
            "propertyPath" : "/properties/NodeType"
          },
          "type" : "string"
        },
        "NumberOfNodes" : {
          "relationshipRef" : {
            "typeName" : "AWS::Redshift::Cluster",
            "propertyPath" : "/properties/NumberOfNodes"
          },
          "type" : "integer"
        },
        "ClusterType" : {
          "relationshipRef" : {
            "typeName" : "AWS::Redshift::Cluster",
            "propertyPath" : "/properties/ClusterType"
          },
          "type" : "string"
        },
        "Classic" : {
          "type" : "boolean"
        },
        "ClusterIdentifier" : {
          "relationshipRef" : {
            "typeName" : "AWS::Redshift::Cluster",
            "propertyPath" : "/properties/ClusterIdentifier"
          },
          "type" : "string"
        }
      },
      "required" : [ "ClusterIdentifier" ]
    },
    "PauseClusterMessage" : {
      "description" : "Describes a pause cluster operation. For example, a scheduled action to run the `PauseCluster` API operation.",
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "ClusterIdentifier" : {
          "relationshipRef" : {
            "typeName" : "AWS::Redshift::Cluster",
            "propertyPath" : "/properties/ClusterIdentifier"
          },
          "type" : "string"
        }
      },
      "required" : [ "ClusterIdentifier" ]
    },
    "ResumeClusterMessage" : {
      "description" : "Describes a resume cluster operation. For example, a scheduled action to run the `ResumeCluster` API operation.",
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "ClusterIdentifier" : {
          "relationshipRef" : {
            "typeName" : "AWS::Redshift::Cluster",
            "propertyPath" : "/properties/ClusterIdentifier"
          },
          "type" : "string"
        }
      },
      "required" : [ "ClusterIdentifier" ]
    },
    "timestamp" : {
      "type" : "string"
    }
  },
  "properties" : {
    "ScheduledActionDescription" : {
      "description" : "The description of the scheduled action.",
      "type" : "string"
    },
    "ScheduledActionName" : {
      "description" : "The name of the scheduled action. The name must be unique within an account.",
      "type" : "string"
    },
    "EndTime" : {
      "description" : "The end time in UTC of the scheduled action. After this time, the scheduled action does not trigger.",
      "$ref" : "#/definitions/timestamp"
    },
    "State" : {
      "description" : "The state of the scheduled action.",
      "type" : "string",
      "enum" : [ "ACTIVE", "DISABLED" ]
    },
    "Schedule" : {
      "description" : "The schedule in `at( )` or `cron( )` format.",
      "type" : "string"
    },
    "IamRole" : {
      "description" : "The IAM role to assume to run the target action.",
      "type" : "string"
    },
    "StartTime" : {
      "description" : "The start time in UTC of the scheduled action. Before this time, the scheduled action does not trigger.",
      "$ref" : "#/definitions/timestamp"
    },
    "Enable" : {
      "description" : "If True, the schedule is enabled. If False, the scheduled action does not trigger.",
      "type" : "boolean"
    },
    "TargetAction" : {
      "description" : "A JSON format string of the Amazon Redshift API operation with input parameters.",
      "$ref" : "#/definitions/ScheduledActionType"
    },
    "NextInvocations" : {
      "description" : "List of times when the scheduled action will run.",
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/timestamp"
      }
    }
  },
  "required" : [ "ScheduledActionName" ]
}