SCHEMA = {
  "$schema" : "https://schema.cloudformation.us-east-1.amazonaws.com/provider.definition.schema.v1.json",
  "typeName" : "AWS::GameLift::GameServerGroup",
  "description" : "The AWS::GameLift::GameServerGroup resource creates an Amazon GameLift (GameLift) GameServerGroup.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-gamelift.git",
  "tagging" : {
    "taggable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "permissions" : [ "gamelift:ListTagsForResource", "gamelift:TagResource", "gamelift:UntagResource" ]
  },
  "definitions" : {
    "AutoScalingPolicy" : {
      "type" : "object",
      "description" : "Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.",
      "properties" : {
        "EstimatedInstanceWarmup" : {
          "$ref" : "#/definitions/EstimatedInstanceWarmup"
        },
        "TargetTrackingConfiguration" : {
          "$ref" : "#/definitions/TargetTrackingConfiguration"
        }
      },
      "required" : [ "TargetTrackingConfiguration" ],
      "additionalProperties" : False
    },
    "EstimatedInstanceWarmup" : {
      "type" : "number",
      "description" : "Length of time, in seconds, it takes for a new instance to start new game server processes and register with GameLift FleetIQ."
    },
    "TargetTrackingConfiguration" : {
      "type" : "object",
      "description" : "Settings for a target-based scaling policy applied to Auto Scaling group.",
      "properties" : {
        "TargetValue" : {
          "$ref" : "#/definitions/TargetValue"
        }
      },
      "required" : [ "TargetValue" ],
      "additionalProperties" : False
    },
    "TargetValue" : {
      "type" : "number",
      "description" : "Desired value to use with a game server group target-based scaling policy."
    },
    "BalancingStrategy" : {
      "type" : "string",
      "description" : "The fallback balancing method to use for the game server group when Spot Instances in a Region become unavailable or are not viable for game hosting.",
      "enum" : [ "SPOT_ONLY", "SPOT_PREFERRED", "ON_DEMAND_ONLY" ]
    },
    "DeleteOption" : {
      "description" : "The type of delete to perform.",
      "type" : "string",
      "enum" : [ "SAFE_DELETE", "FORCE_DELETE", "RETAIN" ]
    },
    "GameServerGroupName" : {
      "type" : "string",
      "description" : "An identifier for the new game server group.",
      "pattern" : "[a-zA-Z0-9-\\.]+",
      "minLength" : 1,
      "maxLength" : 128
    },
    "GameServerProtectionPolicy" : {
      "type" : "string",
      "description" : "A flag that indicates whether instances in the game server group are protected from early termination.",
      "enum" : [ "NO_PROTECTION", "FULL_PROTECTION" ]
    },
    "GameServerGroupArn" : {
      "description" : "A generated unique ID for the game server group.",
      "type" : "string",
      "pattern" : "^arn:.*:gameservergroup\\/[a-zA-Z0-9-\\.]*",
      "minLength" : 1,
      "maxLength" : 256
    },
    "InstanceDefinitions" : {
      "type" : "array",
      "description" : "A set of EC2 instance types to use when creating instances in the group.",
      "items" : {
        "$ref" : "#/definitions/InstanceDefinition"
      },
      "maxItems" : 20,
      "minItems" : 2,
      "insertionOrder" : False
    },
    "InstanceDefinition" : {
      "type" : "object",
      "description" : "An allowed instance type for your game server group.",
      "properties" : {
        "InstanceType" : {
          "$ref" : "#/definitions/InstanceType"
        },
        "WeightedCapacity" : {
          "$ref" : "#/definitions/WeightedCapacity"
        }
      },
      "required" : [ "InstanceType" ],
      "additionalProperties" : False
    },
    "InstanceType" : {
      "type" : "string",
      "description" : "An EC2 instance type designation."
    },
    "WeightedCapacity" : {
      "type" : "string",
      "description" : "Instance weighting that indicates how much this instance type contributes to the total capacity of a game server group.",
      "pattern" : "^[\\u0031-\\u0039][\\u0030-\\u0039]{0,2}$"
    },
    "LaunchTemplate" : {
      "type" : "object",
      "description" : "The EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.",
      "properties" : {
        "LaunchTemplateId" : {
          "$ref" : "#/definitions/LaunchTemplateId"
        },
        "LaunchTemplateName" : {
          "$ref" : "#/definitions/LaunchTemplateName"
        },
        "Version" : {
          "$ref" : "#/definitions/Version"
        }
      },
      "additionalProperties" : False
    },
    "LaunchTemplateId" : {
      "type" : "string",
      "description" : "A unique identifier for an existing EC2 launch template."
    },
    "LaunchTemplateName" : {
      "type" : "string",
      "description" : "A readable identifier for an existing EC2 launch template."
    },
    "Version" : {
      "type" : "string",
      "description" : "The version of the EC2 launch template to use."
    },
    "MaxSize" : {
      "type" : "number",
      "description" : "The maximum number of instances allowed in the EC2 Auto Scaling group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.",
      "minimum" : 1
    },
    "MinSize" : {
      "type" : "number",
      "description" : "The minimum number of instances allowed in the EC2 Auto Scaling group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.",
      "minimum" : 0
    },
    "RoleArn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups.",
      "pattern" : "^arn:.*:role\\/[\\w+=,.@-]+",
      "minLength" : 1,
      "maxLength" : 256
    },
    "Tags" : {
      "type" : "array",
      "description" : "A list of labels to assign to the new game server group resource.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "minItems" : 0,
      "maxItems" : 200,
      "insertionOrder" : False
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key for a developer-defined key:value pair for tagging an AWS resource."
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for a developer-defined key:value pair for tagging an AWS resource."
        }
      },
      "additionalProperties" : False
    },
    "VpcSubnets" : {
      "type" : "array",
      "description" : "A list of virtual private cloud (VPC) subnets to use with instances in the game server group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.",
      "items" : {
        "type" : "string",
        "pattern" : "^subnet-[0-9a-z]+$",
        "minLength" : 15,
        "maxLength" : 24
      },
      "minItems" : 1,
      "maxItems" : 20,
      "insertionOrder" : False
    },
    "GameServerGroup" : {
      "type" : "object",
      "description" : "Properties that describe a game server group resource. A game server group manages certain properties of a corresponding EC2 Auto Scaling group.",
      "properties" : {
        "AutoScalingGroupArn" : {
          "$ref" : "#/definitions/AutoScalingGroupArn"
        },
        "BalancingStrategy" : {
          "$ref" : "#/definitions/BalancingStrategy"
        },
        "CreationTime" : {
          "$ref" : "#/definitions/CreationTime"
        },
        "GameServerGroupArn" : {
          "$ref" : "#/definitions/GameServerGroupArn"
        },
        "GameServerGroupName" : {
          "$ref" : "#/definitions/GameServerGroupName"
        },
        "GameServerProtectionPolicy" : {
          "$ref" : "#/definitions/GameServerProtectionPolicy"
        },
        "InstanceDefinitions" : {
          "$ref" : "#/definitions/InstanceDefinitions"
        },
        "LastUpdatedTime" : {
          "$ref" : "#/definitions/LastUpdatedTime"
        },
        "RoleArn" : {
          "$ref" : "#/definitions/RoleArn"
        },
        "Status" : {
          "$ref" : "#/definitions/Status"
        },
        "StatusReason" : {
          "$ref" : "#/definitions/StatusReason"
        },
        "SuspendedActions" : {
          "$ref" : "#/definitions/SuspendedActions"
        }
      },
      "additionalProperties" : False
    },
    "AutoScalingGroupArn" : {
      "type" : "string",
      "description" : "A generated unique ID for the EC2 Auto Scaling group that is associated with this game server group.",
      "minLength" : 0,
      "maxLength" : 256,
      "pattern" : "[ -퟿-�𐀀-􏿿\r\n\t]*"
    },
    "CreationTime" : {
      "type" : "string",
      "description" : "A timestamp that indicates when this data object was created."
    },
    "LastUpdatedTime" : {
      "type" : "string",
      "description" : "A timestamp that indicates when this game server group was last updated."
    },
    "Status" : {
      "type" : "string",
      "description" : "The current status of the game server group.",
      "enum" : [ "NEW", "ACTIVATING", "ACTIVE", "DELETE_SCHEDULED", "DELETING", "DELETED", "ERROR" ]
    },
    "StatusReason" : {
      "type" : "string",
      "description" : "Additional information about the current game server group status.",
      "minLength" : 1,
      "maxLength" : 1024
    },
    "SuspendedActions" : {
      "type" : "array",
      "items" : {
        "type" : "string",
        "enum" : [ "REPLACE_INSTANCE_TYPES" ]
      }
    }
  },
  "properties" : {
    "AutoScalingGroupArn" : {
      "description" : "A generated unique ID for the EC2 Auto Scaling group that is associated with this game server group.",
      "$ref" : "#/definitions/AutoScalingGroupArn"
    },
    "AutoScalingPolicy" : {
      "description" : "Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.",
      "$ref" : "#/definitions/AutoScalingPolicy"
    },
    "BalancingStrategy" : {
      "description" : "The fallback balancing method to use for the game server group when Spot Instances in a Region become unavailable or are not viable for game hosting.",
      "$ref" : "#/definitions/BalancingStrategy"
    },
    "DeleteOption" : {
      "description" : "The type of delete to perform.",
      "$ref" : "#/definitions/DeleteOption"
    },
    "GameServerGroupArn" : {
      "description" : "A generated unique ID for the game server group.",
      "$ref" : "#/definitions/GameServerGroupArn"
    },
    "GameServerGroupName" : {
      "description" : "An identifier for the new game server group.",
      "$ref" : "#/definitions/GameServerGroupName"
    },
    "GameServerProtectionPolicy" : {
      "description" : "A flag that indicates whether instances in the game server group are protected from early termination.",
      "$ref" : "#/definitions/GameServerProtectionPolicy"
    },
    "InstanceDefinitions" : {
      "description" : "A set of EC2 instance types to use when creating instances in the group.",
      "$ref" : "#/definitions/InstanceDefinitions"
    },
    "LaunchTemplate" : {
      "description" : "The EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.",
      "$ref" : "#/definitions/LaunchTemplate"
    },
    "MaxSize" : {
      "description" : "The maximum number of instances allowed in the EC2 Auto Scaling group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.",
      "$ref" : "#/definitions/MaxSize"
    },
    "MinSize" : {
      "description" : "The minimum number of instances allowed in the EC2 Auto Scaling group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.",
      "$ref" : "#/definitions/MinSize"
    },
    "RoleArn" : {
      "description" : "The Amazon Resource Name (ARN) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups.",
      "$ref" : "#/definitions/RoleArn"
    },
    "Tags" : {
      "description" : "A list of labels to assign to the new game server group resource. Updating game server group tags with CloudFormation will not take effect. Please update this property using AWS GameLift APIs instead.",
      "$ref" : "#/definitions/Tags"
    },
    "VpcSubnets" : {
      "description" : "A list of virtual private cloud (VPC) subnets to use with instances in the game server group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.",
      "$ref" : "#/definitions/VpcSubnets"
    }
  },
  "required" : [ "GameServerGroupName", "InstanceDefinitions", "RoleArn" ],
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/GameServerGroupArn", "/properties/AutoScalingGroupArn" ],
  "writeOnlyProperties" : [ "/properties/DeleteOption", "/properties/LaunchTemplate", "/properties/MinSize", "/properties/MaxSize", "/properties/AutoScalingPolicy", "/properties/VpcSubnets" ],
  "primaryIdentifier" : [ "/properties/GameServerGroupArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "gamelift:CreateGameServerGroup", "gamelift:ListTagsForResource", "gamelift:TagResource", "gamelift:DescribeGameServerGroup", "iam:assumeRole", "iam:PassRole", "iam:CreateServiceLinkedRole", "ec2:DescribeAvailabilityZones", "ec2:DescribeSubnets", "ec2:RunInstances", "ec2:CreateTags", "ec2:DescribeLaunchTemplateVersions", "autoscaling:CreateAutoScalingGroup", "autoscaling:DescribeLifecycleHooks", "autoscaling:DescribeNotificationConfigurations", "autoscaling:CreateAutoScalingGroup", "autoscaling:CreateOrUpdateTags", "autoscaling:DescribeAutoScalingGroups", "autoscaling:ExitStandby", "autoscaling:PutLifecycleHook", "autoscaling:PutScalingPolicy", "autoscaling:ResumeProcesses", "autoscaling:SetInstanceProtection", "autoscaling:UpdateAutoScalingGroup", "events:PutRule", "events:PutTargets" ]
    },
    "read" : {
      "permissions" : [ "gamelift:DescribeGameServerGroup", "gamelift:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "gamelift:UpdateGameServerGroup", "gamelift:TagResource", "gamelift:UntagResource", "gamelift:ListTagsForResource", "iam:assumeRole", "iam:PassRole", "autoscaling:DescribeAutoScalingGroups", "autoscaling:UpdateAutoScalingGroup", "autoscaling:SetInstanceProtection" ]
    },
    "delete" : {
      "permissions" : [ "gamelift:DeleteGameServerGroup", "gamelift:DescribeGameServerGroup", "iam:assumeRole", "iam:PassRole", "iam:CreateServiceLinkedRole", "ec2:DescribeAvailabilityZones", "ec2:DescribeSubnets", "ec2:DescribeLaunchTemplateVersions", "autoscaling:CreateAutoScalingGroup", "autoscaling:DescribeLifecycleHooks", "autoscaling:DescribeNotificationConfigurations", "autoscaling:DescribeAutoScalingGroups", "autoscaling:ExitStandby", "autoscaling:PutLifecycleHook", "autoscaling:PutScalingPolicy", "autoscaling:ResumeProcesses", "autoscaling:SetInstanceProtection", "autoscaling:UpdateAutoScalingGroup", "autoscaling:DeleteAutoScalingGroup", "events:PutRule", "events:PutTargets" ]
    },
    "list" : {
      "permissions" : [ "gamelift:ListGameServerGroups" ]
    }
  }
}