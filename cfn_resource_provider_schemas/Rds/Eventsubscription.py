SCHEMA = {
  "typeName" : "AWS::RDS::EventSubscription",
  "description" : "The ``AWS::RDS::EventSubscription`` resource allows you to receive notifications for Amazon Relational Database Service events through the Amazon Simple Notification Service (Amazon SNS). For more information, see [Using Amazon RDS Event Notification](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html) in the *Amazon RDS User Guide*.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-rds",
  "definitions" : {
    "Tag" : {
      "description" : "Metadata assigned to an Amazon RDS resource consisting of a key-value pair.\n For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with ``aws:`` or ``rds:``. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', ':', '/', '=', '+', '-', '@' (Java regex: \"^([\\\\p{L}\\\\p{Z}\\\\p{N}_.:/=+\\\\-@]*)$\").",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with ``aws:`` or ``rds:``. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', ':', '/', '=', '+', '-', '@' (Java regex: \"^([\\\\p{L}\\\\p{Z}\\\\p{N}_.:/=+\\\\-@]*)$\").",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "additionalProperties" : False,
      "required" : [ "Key" ]
    }
  },
  "properties" : {
    "Tags" : {
      "description" : "An optional array of key-value pairs to apply to this subscription.",
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "SubscriptionName" : {
      "description" : "The name of the subscription.\n Constraints: The name must be less than 255 characters.",
      "type" : "string",
      "maxLength" : 255
    },
    "Enabled" : {
      "description" : "Specifies whether to activate the subscription. If the event notification subscription isn't activated, the subscription is created but not active.",
      "type" : "boolean",
      "default" : True
    },
    "EventCategories" : {
      "description" : "A list of event categories for a particular source type (``SourceType``) that you want to subscribe to. You can see a list of the categories for a given source type in the \"Amazon RDS event categories and event messages\" section of the [Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Messages.html) or the [Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.Messages.html). You can also see this list by using the ``DescribeEventCategories`` operation.",
      "type" : "array",
      "uniqueItems" : True,
      "items" : {
        "type" : "string"
      }
    },
    "SnsTopicArn" : {
      "description" : "The Amazon Resource Name (ARN) of the SNS topic created for event notification. SNS automatically creates the ARN when you create a topic and subscribe to it.\n  RDS doesn't support FIFO (first in, first out) topics. For more information, see [Message ordering and deduplication (FIFO topics)](https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html) in the *Amazon Simple Notification Service Developer Guide*.",
      "type" : "string"
    },
    "SourceIds" : {
      "description" : "The list of identifiers of the event sources for which events are returned. If not specified, then all sources are included in the response. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens. It can't end with a hyphen or contain two consecutive hyphens.\n Constraints:\n  +  If ``SourceIds`` are supplied, ``SourceType`` must also be provided.\n  +  If the source type is a DB instance, a ``DBInstanceIdentifier`` value must be supplied.\n  +  If the source type is a DB cluster, a ``DBClusterIdentifier`` value must be supplied.\n  +  If the source type is a DB parameter group, a ``DBParameterGroupName`` value must be supplied.\n  +  If the source type is a DB security group, a ``DBSecurityGroupName`` value must be supplied.\n  +  If the source type is a DB snapshot, a ``DBSnapshotIdentifier`` value must be supplied.\n  +  If the source type is a DB cluster snapshot, a ``DBClusterSnapshotIdentifier`` value must be supplied.\n  +  If the source type is an RDS Proxy, a ``DBProxyName`` value must be supplied.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "SourceType" : {
      "description" : "The type of source that is generating the events. For example, if you want to be notified of events generated by a DB instance, you set this parameter to ``db-instance``. For RDS Proxy events, specify ``db-proxy``. If this value isn't specified, all events are returned.\n Valid Values:``db-instance | db-cluster | db-parameter-group | db-security-group | db-snapshot | db-cluster-snapshot | db-proxy | zero-etl | custom-engine-version | blue-green-deployment``",
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "propertyTransform" : {
    "/properties/SubscriptionName" : "$lowercase(SubscriptionName)"
  },
  "required" : [ "SnsTopicArn" ],
  "createOnlyProperties" : [ "/properties/SubscriptionName", "/properties/SnsTopicArn" ],
  "primaryIdentifier" : [ "/properties/SubscriptionName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:CreateServiceLinkedRole", "rds:CreateEventSubscription", "rds:DescribeEventSubscriptions", "rds:ListTagsForResource", "rds:AddTagsToResource", "rds:RemoveTagsFromResource" ]
    },
    "read" : {
      "permissions" : [ "rds:DescribeEventSubscriptions", "rds:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "rds:ModifyEventSubscription", "rds:AddSourceIdentifierToSubscription", "rds:RemoveSourceIdentifierFromSubscription", "rds:DescribeEventSubscriptions", "rds:ListTagsForResource", "rds:AddTagsToResource", "rds:RemoveTagsFromResource" ]
    },
    "delete" : {
      "permissions" : [ "rds:DeleteEventSubscription", "rds:DescribeEventSubscriptions" ]
    },
    "list" : {
      "permissions" : [ "rds:DescribeEventSubscriptions" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "rds:AddTagsToResource", "rds:RemoveTagsFromResource" ]
  }
}