SCHEMA = {
  "typeName" : "AWS::SupportApp::SlackChannelConfiguration",
  "description" : "An AWS Support App resource that creates, updates, lists and deletes Slack channel configurations.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-supportapp.git",
  "properties" : {
    "TeamId" : {
      "description" : "The team ID in Slack, which uniquely identifies a workspace.",
      "type" : "string",
      "pattern" : "^\\S+$",
      "minLength" : 1,
      "maxLength" : 256
    },
    "ChannelId" : {
      "description" : "The channel ID in Slack, which identifies a channel within a workspace.",
      "type" : "string",
      "pattern" : "^\\S+$",
      "minLength" : 1,
      "maxLength" : 256
    },
    "ChannelName" : {
      "description" : "The channel name in Slack.",
      "type" : "string",
      "pattern" : "^.+$",
      "minLength" : 1,
      "maxLength" : 256
    },
    "NotifyOnCreateOrReopenCase" : {
      "description" : "Whether to notify when a case is created or reopened.",
      "type" : "boolean"
    },
    "NotifyOnAddCorrespondenceToCase" : {
      "description" : "Whether to notify when a correspondence is added to a case.",
      "type" : "boolean"
    },
    "NotifyOnResolveCase" : {
      "description" : "Whether to notify when a case is resolved.",
      "type" : "boolean"
    },
    "NotifyOnCaseSeverity" : {
      "description" : "The severity level of a support case that a customer wants to get notified for.",
      "type" : "string",
      "enum" : [ "none", "all", "high" ]
    },
    "ChannelRoleArn" : {
      "description" : "The Amazon Resource Name (ARN) of an IAM role that grants the AWS Support App access to perform operations for AWS services.",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:iam::[0-9]{12}:role\\/(.+)$",
      "minLength" : 31,
      "maxLength" : 2048
    }
  },
  "required" : [ "TeamId", "ChannelId", "NotifyOnCaseSeverity", "ChannelRoleArn" ],
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/TeamId", "/properties/ChannelId" ],
  "createOnlyProperties" : [ "/properties/TeamId", "/properties/ChannelId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "supportapp:CreateSlackChannelConfiguration", "supportapp:ListSlackChannelConfigurations" ]
    },
    "read" : {
      "permissions" : [ "supportapp:ListSlackChannelConfigurations" ]
    },
    "update" : {
      "permissions" : [ "supportapp:UpdateSlackChannelConfiguration", "supportapp:ListSlackChannelConfigurations" ]
    },
    "delete" : {
      "permissions" : [ "supportapp:DeleteSlackChannelConfiguration", "supportapp:ListSlackChannelConfigurations" ]
    },
    "list" : {
      "permissions" : [ "supportapp:ListSlackChannelConfigurations" ]
    }
  }
}