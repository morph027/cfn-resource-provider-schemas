SCHEMA = {
  "$schema" : "https://raw.githubusercontent.com/aws-cloudformation/cloudformation-resource-schema/master/src/main/resources/schema/provider.definition.schema.v1.json",
  "typeName" : "AWS::AutoScaling::LifecycleHook",
  "description" : "Resource Type definition for AWS::AutoScaling::LifecycleHook",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-autoscaling.git",
  "properties" : {
    "AutoScalingGroupName" : {
      "description" : "The name of the Auto Scaling group for the lifecycle hook.",
      "type" : "string"
    },
    "DefaultResult" : {
      "description" : "The action the Auto Scaling group takes when the lifecycle hook timeout elapses or if an unexpected failure occurs. The valid values are CONTINUE and ABANDON (default).",
      "type" : "string"
    },
    "HeartbeatTimeout" : {
      "description" : "The maximum time, in seconds, that can elapse before the lifecycle hook times out. The range is from 30 to 7200 seconds. The default value is 3600 seconds (1 hour). If the lifecycle hook times out, Amazon EC2 Auto Scaling performs the action that you specified in the DefaultResult property.",
      "type" : "integer"
    },
    "LifecycleHookName" : {
      "description" : "The name of the lifecycle hook.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "LifecycleTransition" : {
      "description" : "The instance state to which you want to attach the lifecycle hook.",
      "type" : "string"
    },
    "NotificationMetadata" : {
      "description" : "Additional information that is included any time Amazon EC2 Auto Scaling sends a message to the notification target.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 1023
    },
    "NotificationTargetARN" : {
      "description" : "The Amazon Resource Name (ARN) of the notification target that Amazon EC2 Auto Scaling uses to notify you when an instance is in the transition state for the lifecycle hook. You can specify an Amazon SQS queue or an Amazon SNS topic. The notification message includes the following information: lifecycle action token, user account ID, Auto Scaling group name, lifecycle hook name, instance ID, lifecycle transition, and notification metadata.",
      "type" : "string"
    },
    "RoleARN" : {
      "description" : "The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target, for example, an Amazon SNS topic or an Amazon SQS queue.",
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "required" : [ "LifecycleTransition", "AutoScalingGroupName" ],
  "createOnlyProperties" : [ "/properties/AutoScalingGroupName", "/properties/LifecycleHookName" ],
  "primaryIdentifier" : [ "/properties/AutoScalingGroupName", "/properties/LifecycleHookName" ],
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "autoscaling:PutLifecycleHook", "autoscaling:DescribeLifecycleHooks", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "autoscaling:DescribeLifecycleHooks" ]
    },
    "update" : {
      "permissions" : [ "autoscaling:PutLifecycleHook", "autoscaling:DescribeLifecycleHooks", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "autoscaling:DeleteLifecycleHook", "autoscaling:DescribeLifecycleHooks" ]
    },
    "list" : {
      "permissions" : [ "autoscaling:DescribeLifecycleHooks" ]
    }
  }
}