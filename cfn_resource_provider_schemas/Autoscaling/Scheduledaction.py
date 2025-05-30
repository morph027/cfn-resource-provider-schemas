SCHEMA = {
  "typeName" : "AWS::AutoScaling::ScheduledAction",
  "description" : "The AWS::AutoScaling::ScheduledAction resource specifies an Amazon EC2 Auto Scaling scheduled action so that the Auto Scaling group can change the number of instances available for your application in response to predictable load changes.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "properties" : {
    "ScheduledActionName" : {
      "description" : "Auto-generated unique identifier",
      "type" : "string"
    },
    "MinSize" : {
      "description" : "The minimum size of the Auto Scaling group.",
      "type" : "integer"
    },
    "Recurrence" : {
      "description" : "The recurring schedule for the action, in Unix cron syntax format. When StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action starts and stops.",
      "type" : "string"
    },
    "TimeZone" : {
      "description" : "The time zone for the cron expression.",
      "type" : "string"
    },
    "EndTime" : {
      "description" : "The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.",
      "type" : "string"
    },
    "AutoScalingGroupName" : {
      "description" : "The name of the Auto Scaling group.",
      "type" : "string"
    },
    "StartTime" : {
      "description" : "The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.",
      "type" : "string"
    },
    "DesiredCapacity" : {
      "description" : "The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.",
      "type" : "integer"
    },
    "MaxSize" : {
      "description" : "The minimum size of the Auto Scaling group.",
      "type" : "integer"
    }
  },
  "additionalProperties" : False,
  "required" : [ "AutoScalingGroupName" ],
  "createOnlyProperties" : [ "/properties/AutoScalingGroupName" ],
  "primaryIdentifier" : [ "/properties/ScheduledActionName", "/properties/AutoScalingGroupName" ],
  "readOnlyProperties" : [ "/properties/ScheduledActionName" ],
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "autoscaling:PutScheduledUpdateGroupAction", "autoscaling:DescribeScheduledActions" ]
    },
    "read" : {
      "permissions" : [ "autoscaling:DescribeScheduledActions" ]
    },
    "update" : {
      "permissions" : [ "autoscaling:PutScheduledUpdateGroupAction" ]
    },
    "delete" : {
      "permissions" : [ "autoscaling:DeleteScheduledAction", "autoscaling:DescribeScheduledActions" ]
    },
    "list" : {
      "permissions" : [ "autoscaling:DescribeScheduledActions" ]
    }
  }
}