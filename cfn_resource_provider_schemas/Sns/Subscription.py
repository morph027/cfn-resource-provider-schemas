SCHEMA = {
  "typeName" : "AWS::SNS::Subscription",
  "description" : "Resource Type definition for AWS::SNS::Subscription",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-sns",
  "additionalProperties" : False,
  "properties" : {
    "Arn" : {
      "type" : "string",
      "description" : "Arn of the subscription"
    },
    "ReplayPolicy" : {
      "type" : [ "object", "string" ],
      "description" : "Specifies whether Amazon SNS resends the notification to the subscription when a message's attribute changes."
    },
    "RawMessageDelivery" : {
      "type" : "boolean",
      "description" : "When set to True, enables raw message delivery. Raw messages don't contain any JSON formatting and can be sent to Amazon SQS and HTTP/S endpoints."
    },
    "Endpoint" : {
      "type" : "string",
      "description" : "The subscription's endpoint. The endpoint value depends on the protocol that you specify. "
    },
    "FilterPolicy" : {
      "type" : [ "object", "string" ],
      "description" : "The filter policy JSON assigned to the subscription. Enables the subscriber to filter out unwanted messages."
    },
    "TopicArn" : {
      "type" : "string",
      "description" : "The ARN of the topic to subscribe to."
    },
    "RedrivePolicy" : {
      "type" : [ "object", "string" ],
      "description" : "When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue. Messages that can't be delivered due to client errors are held in the dead-letter queue for further analysis or reprocessing."
    },
    "DeliveryPolicy" : {
      "type" : [ "object", "string" ],
      "description" : "The delivery policy JSON assigned to the subscription. Enables the subscriber to define the message delivery retry strategy in the case of an HTTP/S endpoint subscribed to the topic."
    },
    "Region" : {
      "type" : "string",
      "description" : "For cross-region subscriptions, the region in which the topic resides.If no region is specified, AWS CloudFormation uses the region of the caller as the default."
    },
    "SubscriptionRoleArn" : {
      "type" : "string",
      "description" : "This property applies only to Amazon Data Firehose delivery stream subscriptions."
    },
    "FilterPolicyScope" : {
      "type" : "string",
      "description" : "This attribute lets you choose the filtering scope by using one of the following string value types: MessageAttributes (default) and MessageBody."
    },
    "Protocol" : {
      "type" : "string",
      "description" : "The subscription's protocol."
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "required" : [ "TopicArn", "Protocol" ],
  "createOnlyProperties" : [ "/properties/Endpoint", "/properties/Protocol", "/properties/TopicArn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "conditionalCreateOnlyProperties" : [ "/properties/Region" ],
  "writeOnlyProperties" : [ "/properties/Region" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:GetRole", "iam:PassRole", "sns:Subscribe" ]
    },
    "read" : {
      "permissions" : [ "sns:GetSubscriptionAttributes" ]
    },
    "update" : {
      "permissions" : [ "iam:GetRole", "iam:PassRole", "sns:SetSubscriptionAttributes" ]
    },
    "delete" : {
      "permissions" : [ "sns:Unsubscribe", "sns:GetSubscriptionAttributes" ]
    },
    "list" : {
      "permissions" : [ "sns:ListSubscriptions" ]
    }
  }
}