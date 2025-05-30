SCHEMA = {
  "typeName" : "AWS::ResilienceHub::App",
  "description" : "Resource Type Definition for AWS::ResilienceHub::App.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-resiliencehub",
  "definitions" : {
    "TagValue" : {
      "type" : "string",
      "maxLength" : 256
    },
    "TagMap" : {
      "type" : "object",
      "patternProperties" : {
        ".{1,128}" : {
          "$ref" : "#/definitions/TagValue"
        }
      },
      "additionalProperties" : False
    },
    "PhysicalResourceId" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AwsAccountId" : {
          "type" : "string",
          "pattern" : "^[0-9]{12}$"
        },
        "AwsRegion" : {
          "type" : "string",
          "pattern" : "^[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]$"
        },
        "Identifier" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 255
        },
        "Type" : {
          "type" : "string",
          "pattern" : "Arn|Native"
        }
      },
      "required" : [ "Identifier", "Type" ]
    },
    "ResourceMapping" : {
      "description" : "Resource mapping is used to map logical resources from template to physical resource",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "LogicalStackName" : {
          "type" : "string"
        },
        "MappingType" : {
          "type" : "string",
          "pattern" : "CfnStack|Resource|Terraform|EKS"
        },
        "ResourceName" : {
          "type" : "string",
          "pattern" : "^[A-Za-z0-9][A-Za-z0-9_\\-]{1,59}$"
        },
        "TerraformSourceName" : {
          "type" : "string"
        },
        "EksSourceName" : {
          "type" : "string"
        },
        "PhysicalResourceId" : {
          "$ref" : "#/definitions/PhysicalResourceId"
        }
      },
      "required" : [ "MappingType", "PhysicalResourceId" ]
    },
    "IamRoleArn" : {
      "type" : "string",
      "pattern" : "arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):iam::[0-9]{12}:role\\/(([\\u0021-\\u007E]+\\u002F){1,511})?[A-Za-z0-9+=,.@_/-]{1,64}$"
    },
    "PermissionModel" : {
      "description" : "Defines the roles and credentials that AWS Resilience Hub would use while creating the application, importing its resources, and running an assessment.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Type" : {
          "description" : "Defines how AWS Resilience Hub scans your resources. It can scan for the resources by using a pre-existing role in your AWS account, or by using the credentials of the current IAM user.",
          "type" : "string",
          "enum" : [ "LegacyIAMUser", "RoleBased" ]
        },
        "InvokerRoleName" : {
          "description" : "Existing AWS IAM role name in the primary AWS account that will be assumed by AWS Resilience Hub Service Principle to obtain a read-only access to your application resources while running an assessment.",
          "type" : "string",
          "pattern" : "((\\u002F[\\u0021-\\u007E]+\\u002F){1,511})?[A-Za-z0-9+=,.@_/-]{1,64}"
        },
        "CrossAccountRoleArns" : {
          "description" : "Defines a list of role Amazon Resource Names (ARNs) to be used in other accounts. These ARNs are used for querying purposes while importing resources and assessing your application.",
          "type" : "array",
          "uniqueItems" : False,
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/IamRoleArn"
          }
        }
      },
      "required" : [ "Type" ]
    },
    "EventSubscription" : {
      "description" : "Indicates an event you would like to subscribe and get notification for.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Name" : {
          "description" : "Unique name to identify an event subscription.",
          "type" : "string",
          "maxLength" : 256
        },
        "EventType" : {
          "description" : "The type of event you would like to subscribe and get notification for.",
          "type" : "string",
          "enum" : [ "ScheduledAssessmentFailure", "DriftDetected" ]
        },
        "SnsTopicArn" : {
          "description" : "Amazon Resource Name (ARN) of the Amazon Simple Notification Service topic.",
          "type" : "string",
          "pattern" : "^arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}$"
        }
      },
      "required" : [ "Name", "EventType" ]
    }
  },
  "properties" : {
    "Name" : {
      "description" : "Name of the app.",
      "type" : "string",
      "pattern" : "^[A-Za-z0-9][A-Za-z0-9_\\-]{1,59}$"
    },
    "Description" : {
      "description" : "App description.",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 500
    },
    "AppArn" : {
      "type" : "string",
      "description" : "Amazon Resource Name (ARN) of the App.",
      "pattern" : "^arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$"
    },
    "ResiliencyPolicyArn" : {
      "type" : "string",
      "description" : "Amazon Resource Name (ARN) of the Resiliency Policy.",
      "pattern" : "^arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$"
    },
    "Tags" : {
      "$ref" : "#/definitions/TagMap"
    },
    "AppTemplateBody" : {
      "description" : "A string containing full ResilienceHub app template body.",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 409600,
      "pattern" : "^[\\w\\s:,-\\.'\\/{}\\[\\]:\"]+$"
    },
    "ResourceMappings" : {
      "description" : "An array of ResourceMapping objects.",
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/ResourceMapping"
      }
    },
    "AppAssessmentSchedule" : {
      "description" : "Assessment execution schedule.",
      "type" : "string",
      "enum" : [ "Disabled", "Daily" ]
    },
    "PermissionModel" : {
      "$ref" : "#/definitions/PermissionModel"
    },
    "EventSubscriptions" : {
      "description" : "The list of events you would like to subscribe and get notification for.",
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/EventSubscription"
      }
    },
    "DriftStatus" : {
      "description" : "Indicates if compliance drifts (deviations) were detected while running an assessment for your application.",
      "type" : "string",
      "enum" : [ "NotChecked", "NotDetected", "Detected" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "resiliencehub:TagResource", "resiliencehub:ListTagsForResource", "resiliencehub:UntagResource" ]
  },
  "additionalProperties" : False,
  "required" : [ "Name", "AppTemplateBody", "ResourceMappings" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "readOnlyProperties" : [ "/properties/AppArn", "/properties/DriftStatus" ],
  "primaryIdentifier" : [ "/properties/AppArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "cloudformation:DescribeStacks", "cloudformation:ListStackResources", "s3:GetBucketLocation", "s3:GetObject", "s3:ListAllMyBuckets", "autoscaling:DescribeAutoScalingGroups", "apigateway:GET", "ec2:Describe*", "ecs:DescribeServices", "eks:DescribeCluster", "elasticfilesystem:DescribeFileSystems", "elasticloadbalancing:DescribeLoadBalancers", "lambda:GetFunction*", "rds:Describe*", "dynamodb:Describe*", "sqs:GetQueueAttributes", "sns:GetTopicAttributes", "route53:List*", "iam:PassRole", "resiliencehub:CreateApp", "resiliencehub:DescribeApp", "resiliencehub:DescribeAppVersionTemplate", "resiliencehub:PutDraftAppVersionTemplate", "resiliencehub:AddDraftAppVersionResourceMappings", "resiliencehub:ListAppVersionResourceMappings", "resiliencehub:ListAppVersions", "resiliencehub:PublishAppVersion", "resiliencehub:ListTagsForResource", "resiliencehub:TagResource", "resiliencehub:UntagResource" ]
    },
    "read" : {
      "permissions" : [ "resiliencehub:DescribeApp", "resiliencehub:DescribeAppVersionTemplate", "resiliencehub:ListAppVersionResourceMappings", "resiliencehub:ListTagsForResource", "resiliencehub:ListAppVersions" ]
    },
    "update" : {
      "permissions" : [ "cloudformation:DescribeStacks", "cloudformation:ListStackResources", "s3:GetBucketLocation", "s3:GetObject", "s3:ListAllMyBuckets", "autoscaling:DescribeAutoScalingGroups", "apigateway:GET", "ec2:Describe*", "ecs:DescribeServices", "eks:DescribeCluster", "elasticfilesystem:DescribeFileSystems", "elasticloadbalancing:DescribeLoadBalancers", "lambda:GetFunction*", "rds:Describe*", "dynamodb:Describe*", "sqs:GetQueueAttributes", "sns:GetTopicAttributes", "route53:List*", "iam:PassRole", "resiliencehub:UpdateApp", "resiliencehub:DescribeApp", "resiliencehub:DescribeAppVersionTemplate", "resiliencehub:PutDraftAppVersionTemplate", "resiliencehub:AddDraftAppVersionResourceMappings", "resiliencehub:RemoveDraftAppVersionResourceMappings", "resiliencehub:ListAppVersionResourceMappings", "resiliencehub:ListAppVersions", "resiliencehub:PublishAppVersion", "resiliencehub:ListTagsForResource", "resiliencehub:TagResource", "resiliencehub:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "resiliencehub:DeleteApp", "resiliencehub:UntagResource", "resiliencehub:ListApps" ]
    },
    "list" : {
      "permissions" : [ "resiliencehub:ListApps" ]
    }
  }
}