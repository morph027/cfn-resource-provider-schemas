SCHEMA = {
  "typeName" : "AWS::Chatbot::SlackChannelConfiguration",
  "description" : "Resource schema for AWS::Chatbot::SlackChannelConfiguration.",
  "sourceUrl" : "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html",
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "properties" : {
    "SlackWorkspaceId" : {
      "description" : "The id of the Slack workspace",
      "type" : "string",
      "pattern" : "^[0-9A-Z]{1,255}$",
      "minLength" : 1,
      "maxLength" : 256
    },
    "SlackChannelId" : {
      "description" : "The id of the Slack channel",
      "type" : "string",
      "pattern" : "^[A-Za-z0-9]+$",
      "minLength" : 1,
      "maxLength" : 256
    },
    "ConfigurationName" : {
      "description" : "The name of the configuration",
      "type" : "string",
      "pattern" : "^[A-Za-z0-9-_]+$",
      "minLength" : 1,
      "maxLength" : 128
    },
    "IamRoleArn" : {
      "description" : "The ARN of the IAM role that defines the permissions for AWS Chatbot",
      "type" : "string",
      "pattern" : "^arn:(aws[a-zA-Z-]*)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$"
    },
    "SnsTopicArns" : {
      "description" : "ARNs of SNS topics which delivers notifications to AWS Chatbot, for example CloudWatch alarm notifications.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "pattern" : "^arn:(aws[a-zA-Z-]*)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$"
      }
    },
    "LoggingLevel" : {
      "description" : "Specifies the logging level for this configuration:ERROR,INFO or NONE. This property affects the log entries pushed to Amazon CloudWatch logs",
      "type" : "string",
      "pattern" : "^(ERROR|INFO|NONE)$",
      "default" : "NONE"
    },
    "Arn" : {
      "description" : "Amazon Resource Name (ARN) of the configuration",
      "type" : "string",
      "pattern" : "^arn:(aws[a-zA-Z-]*)?:chatbot:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$"
    },
    "GuardrailPolicies" : {
      "description" : "The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "pattern" : "^(^$|arn:aws:iam:[A-Za-z0-9_\\/.-]{0,63}:[A-Za-z0-9_\\/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_\\/+=,@.-]{0,1023})$"
      }
    },
    "Tags" : {
      "description" : "The tags to add to the configuration",
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "UserRoleRequired" : {
      "description" : "Enables use of a user role requirement in your chat configuration",
      "type" : "boolean",
      "default" : False
    },
    "CustomizationResourceArns" : {
      "description" : "ARNs of Custom Actions to associate with notifications in the provided chat channel.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "pattern" : "^arn:aws:chatbot:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:custom-action/[a-zA-Z0-9_-]{1,64}$"
      }
    }
  },
  "required" : [ "SlackWorkspaceId", "SlackChannelId", "ConfigurationName", "IamRoleArn" ],
  "createOnlyProperties" : [ "/properties/SlackWorkspaceId", "/properties/ConfigurationName" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "additionalProperties" : False,
  "handlers" : {
    "create" : {
      "permissions" : [ "chatbot:CreateSlackChannelConfiguration", "chatbot:TagResource", "chatbot:AssociateToConfiguration", "chatbot:ListAssociations", "iam:PassRole", "iam:CreateServiceLinkedRole" ]
    },
    "read" : {
      "permissions" : [ "chatbot:DescribeSlackChannelConfigurations", "chatbot:ListAssociations" ]
    },
    "update" : {
      "permissions" : [ "chatbot:UpdateSlackChannelConfiguration", "chatbot:TagResource", "chatbot:UntagResource", "chatbot:ListTagsForResource", "chatbot:AssociateToConfiguration", "chatbot:DisassociateFromConfiguration", "chatbot:ListAssociations", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "chatbot:DeleteSlackChannelConfiguration", "chatbot:DisassociateFromConfiguration", "chatbot:ListAssociations" ]
    },
    "list" : {
      "permissions" : [ "chatbot:DescribeSlackChannelConfigurations", "chatbot:ListAssociations" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "chatbot:TagResource", "chatbot:ListTagsForResource", "chatbot:UntagResource" ]
  }
}