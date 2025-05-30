SCHEMA = {
  "tagging" : {
    "permissions" : [ "CloudTrail:AddTags", "CloudTrail:RemoveTags", "CloudTrail:ListTags" ],
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "tagProperty" : "/properties/Tags",
    "cloudFormationSystemTags" : False
  },
  "typeName" : "AWS::CloudTrail::Trail",
  "readOnlyProperties" : [ "/properties/Arn", "/properties/SnsTopicArn" ],
  "description" : "Creates a trail that specifies the settings for delivery of log data to an Amazon S3 bucket. A maximum of five trails can exist in a region, irrespective of the region in which they were created.",
  "createOnlyProperties" : [ "/properties/TrailName" ],
  "primaryIdentifier" : [ "/properties/TrailName" ],
  "required" : [ "S3BucketName", "IsLogging" ],
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-cloudtrail.git",
  "propertyTransform" : {
    "/properties/KMSKeyId" : "$join([\"arn:(aws)[-]{0,1}[a-z]{0,2}[-]{0,1}[a-z]{0,3}:kms:[a-z]{2}[-]{1}[a-z]{3,10}[-]{0,1}[a-z]{0,10}[-]{1}[1-3]{1}:[0-9]{12}[:]{1}key\\/\", KMSKeyId])"
  },
  "handlers" : {
    "read" : {
      "permissions" : [ "CloudTrail:GetTrail", "CloudTrail:GetTrailStatus", "CloudTrail:ListTags", "CloudTrail:GetEventSelectors", "CloudTrail:GetInsightSelectors", "CloudTrail:DescribeTrails" ]
    },
    "create" : {
      "permissions" : [ "CloudTrail:CreateTrail", "CloudTrail:StartLogging", "CloudTrail:AddTags", "CloudTrail:PutEventSelectors", "CloudTrail:PutInsightSelectors", "iam:GetRole", "iam:PassRole", "iam:CreateServiceLinkedRole", "organizations:DescribeOrganization", "organizations:ListAWSServiceAccessForOrganization" ]
    },
    "update" : {
      "permissions" : [ "CloudTrail:UpdateTrail", "CloudTrail:StartLogging", "CloudTrail:StopLogging", "CloudTrail:AddTags", "CloudTrail:RemoveTags", "CloudTrail:PutEventSelectors", "CloudTrail:PutInsightSelectors", "iam:GetRole", "iam:PassRole", "iam:CreateServiceLinkedRole", "organizations:DescribeOrganization", "organizations:ListAWSServiceAccessForOrganization", "CloudTrail:GetTrail", "CloudTrail:DescribeTrails" ]
    },
    "list" : {
      "permissions" : [ "CloudTrail:ListTrails", "CloudTrail:GetTrail", "CloudTrail:GetTrailStatus", "CloudTrail:ListTags", "CloudTrail:GetEventSelectors", "CloudTrail:GetInsightSelectors", "CloudTrail:DescribeTrails" ]
    },
    "delete" : {
      "permissions" : [ "CloudTrail:DeleteTrail" ]
    }
  },
  "additionalProperties" : False,
  "definitions" : {
    "AdvancedEventSelector" : {
      "description" : "Advanced event selectors let you create fine-grained selectors for the following AWS CloudTrail event record ﬁelds. They help you control costs by logging only those events that are important to you.",
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "FieldSelectors" : {
          "minItems" : 1,
          "uniqueItems" : True,
          "description" : "Contains all selector statements in an advanced event selector.",
          "insertionOrder" : False,
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/AdvancedFieldSelector"
          }
        },
        "Name" : {
          "minLength" : 1,
          "description" : "An optional, descriptive name for an advanced event selector, such as \"Log data events for only two S3 buckets\".",
          "type" : "string",
          "maxLength" : 1000
        }
      },
      "required" : [ "FieldSelectors" ]
    },
    "InsightSelector" : {
      "description" : "A string that contains insight types that are logged on a trail.",
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "InsightType" : {
          "description" : "The type of insight to log on a trail.",
          "type" : "string"
        }
      }
    },
    "EventSelector" : {
      "description" : "The type of email sending events to publish to the event destination.",
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "IncludeManagementEvents" : {
          "description" : "Specify if you want your event selector to include management events for your trail.",
          "type" : "boolean"
        },
        "ReadWriteType" : {
          "description" : "Specify if you want your trail to log read-only events, write-only events, or all. For example, the EC2 GetConsoleOutput is a read-only API operation and RunInstances is a write-only API operation.",
          "type" : "string",
          "enum" : [ "All", "ReadOnly", "WriteOnly" ]
        },
        "ExcludeManagementEventSources" : {
          "uniqueItems" : True,
          "description" : "An optional list of service event sources from which you do not want management events to be logged on your trail. In this release, the list can be empty (disables the filter), or it can filter out AWS Key Management Service events by containing \"kms.amazonaws.com\". By default, ExcludeManagementEventSources is empty, and AWS KMS events are included in events that are logged to your trail.",
          "insertionOrder" : False,
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        },
        "DataResources" : {
          "uniqueItems" : True,
          "insertionOrder" : False,
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/DataResource"
          }
        }
      }
    },
    "DataResource" : {
      "description" : "CloudTrail supports data event logging for Amazon S3 objects and AWS Lambda functions. You can specify up to 250 resources for an individual event selector, but the total number of data resources cannot exceed 250 across all event selectors in a trail. This limit does not apply if you configure resource logging for all data events.",
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Type" : {
          "description" : "The resource type in which you want to log data events. You can specify AWS::S3::Object or AWS::Lambda::Function resources.",
          "type" : "string"
        },
        "Values" : {
          "uniqueItems" : True,
          "description" : "An array of Amazon Resource Name (ARN) strings or partial ARN strings for the specified objects.",
          "insertionOrder" : False,
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        }
      },
      "required" : [ "Type" ]
    },
    "Tag" : {
      "description" : "An arbitrary set of tags (key-value pairs) for this trail.",
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Value" : {
          "description" : "The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string"
        },
        "Key" : {
          "description" : "The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    },
    "AdvancedFieldSelector" : {
      "description" : "A single selector statement in an advanced event selector.",
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Field" : {
          "minLength" : 1,
          "pattern" : "([\\w|\\d|\\.|_]+)",
          "description" : "A field in an event record on which to filter events to be logged. Supported fields include readOnly, eventCategory, eventSource (for management events), eventName, resources.type, and resources.ARN.",
          "type" : "string",
          "maxLength" : 1000
        },
        "Equals" : {
          "minItems" : 1,
          "uniqueItems" : True,
          "description" : "An operator that includes events that match the exact value of the event record field specified as the value of Field. This is the only valid operator that you can use with the readOnly, eventCategory, and resources.type fields.",
          "insertionOrder" : False,
          "type" : "array",
          "items" : {
            "minLength" : 1,
            "pattern" : "(.+)",
            "type" : "string",
            "maxLength" : 2048
          }
        },
        "NotStartsWith" : {
          "minItems" : 1,
          "uniqueItems" : True,
          "description" : "An operator that excludes events that match the first few characters of the event record field specified as the value of Field.",
          "insertionOrder" : False,
          "type" : "array",
          "items" : {
            "minLength" : 1,
            "pattern" : "(.+)",
            "type" : "string",
            "maxLength" : 2048
          }
        },
        "NotEndsWith" : {
          "minItems" : 1,
          "uniqueItems" : True,
          "description" : "An operator that excludes events that match the last few characters of the event record field specified as the value of Field.",
          "insertionOrder" : False,
          "type" : "array",
          "items" : {
            "minLength" : 1,
            "pattern" : "(.+)",
            "type" : "string",
            "maxLength" : 2048
          }
        },
        "StartsWith" : {
          "minItems" : 1,
          "uniqueItems" : True,
          "description" : "An operator that includes events that match the first few characters of the event record field specified as the value of Field.",
          "insertionOrder" : False,
          "type" : "array",
          "items" : {
            "minLength" : 1,
            "pattern" : "(.+)",
            "type" : "string",
            "maxLength" : 2048
          }
        },
        "EndsWith" : {
          "minItems" : 1,
          "uniqueItems" : True,
          "description" : "An operator that includes events that match the last few characters of the event record field specified as the value of Field.",
          "insertionOrder" : False,
          "type" : "array",
          "items" : {
            "minLength" : 1,
            "pattern" : "(.+)",
            "type" : "string",
            "maxLength" : 2048
          }
        },
        "NotEquals" : {
          "minItems" : 1,
          "uniqueItems" : True,
          "description" : "An operator that excludes events that match the exact value of the event record field specified as the value of Field.",
          "insertionOrder" : False,
          "type" : "array",
          "items" : {
            "minLength" : 1,
            "pattern" : "(.+)",
            "type" : "string",
            "maxLength" : 2048
          }
        }
      },
      "required" : [ "Field" ]
    }
  },
  "properties" : {
    "IncludeGlobalServiceEvents" : {
      "description" : "Specifies whether the trail is publishing events from global services such as IAM to the log files.",
      "type" : "boolean"
    },
    "EventSelectors" : {
      "maxItems" : 5,
      "uniqueItems" : True,
      "description" : "Use event selectors to further specify the management and data event settings for your trail. By default, trails created without specific event selectors will be configured to log all read and write management events, and no data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn't match any event selector, the trail doesn't log the event. You can configure up to five event selectors for a trail.",
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/EventSelector"
      }
    },
    "KMSKeyId" : {
      "description" : "Specifies the KMS key ID to use to encrypt the logs delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.",
      "type" : "string"
    },
    "CloudWatchLogsRoleArn" : {
      "description" : "Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.",
      "type" : "string"
    },
    "S3KeyPrefix" : {
      "description" : "Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see Finding Your CloudTrail Log Files. The maximum length is 200 characters.",
      "type" : "string",
      "maxLength" : 200
    },
    "AdvancedEventSelectors" : {
      "uniqueItems" : True,
      "description" : "The advanced event selectors that were used to select events for the data store.",
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/AdvancedEventSelector"
      }
    },
    "TrailName" : {
      "minLength" : 3,
      "pattern" : "(^[a-zA-Z0-9]$)|(^[a-zA-Z0-9]([a-zA-Z0-9\\._-])*[a-zA-Z0-9]$)",
      "type" : "string",
      "maxLength" : 128
    },
    "IsOrganizationTrail" : {
      "description" : "Specifies whether the trail is created for all accounts in an organization in AWS Organizations, or only for the current AWS account. The default is False, and cannot be True unless the call is made on behalf of an AWS account that is the master account for an organization in AWS Organizations.",
      "type" : "boolean"
    },
    "InsightSelectors" : {
      "uniqueItems" : True,
      "description" : "Lets you enable Insights event logging by specifying the Insights selectors that you want to enable on an existing trail.",
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/InsightSelector"
      }
    },
    "CloudWatchLogsLogGroupArn" : {
      "description" : "Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered. Not required unless you specify CloudWatchLogsRoleArn.",
      "type" : "string"
    },
    "SnsTopicName" : {
      "description" : "Specifies the name of the Amazon SNS topic defined for notification of log file delivery. The maximum length is 256 characters.",
      "type" : "string",
      "maxLength" : 256
    },
    "IsMultiRegionTrail" : {
      "description" : "Specifies whether the trail applies only to the current region or to all regions. The default is False. If the trail exists only in the current region and this value is set to True, shadow trails (replications of the trail) will be created in the other regions. If the trail exists in all regions and this value is set to false, the trail will remain in the region where it was created, and its shadow trails in other regions will be deleted. As a best practice, consider using trails that log events in all regions.",
      "type" : "boolean"
    },
    "S3BucketName" : {
      "description" : "Specifies the name of the Amazon S3 bucket designated for publishing log files. See Amazon S3 Bucket Naming Requirements.",
      "type" : "string"
    },
    "SnsTopicArn" : {
      "type" : "string"
    },
    "EnableLogFileValidation" : {
      "description" : "Specifies whether log file validation is enabled. The default is False.",
      "type" : "boolean"
    },
    "Arn" : {
      "type" : "string"
    },
    "Tags" : {
      "uniqueItems" : False,
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "IsLogging" : {
      "description" : "Whether the CloudTrail is currently logging AWS API calls.",
      "type" : "boolean"
    }
  }
}