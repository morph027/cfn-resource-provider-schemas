SCHEMA = {
  "typeName" : "AWS::WAFv2::LoggingConfiguration",
  "description" : "A WAFv2 Logging Configuration Resource Provider",
  "sourceUrl" : "https://github.com/advaj/aws-cloudformation-resource-providers-wafv2.git",
  "definitions" : {
    "Filter" : {
      "type" : "object",
      "properties" : {
        "Behavior" : {
          "description" : "How to handle logs that satisfy the filter's conditions and requirement. ",
          "type" : "string",
          "enum" : [ "KEEP", "DROP" ]
        },
        "Conditions" : {
          "description" : "Match conditions for the filter.",
          "type" : "array",
          "minItems" : 1,
          "items" : {
            "$ref" : "#/definitions/Condition"
          }
        },
        "Requirement" : {
          "description" : "Logic to apply to the filtering conditions. You can specify that, in order to satisfy the filter, a log must match all conditions or must match at least one condition.",
          "type" : "string",
          "enum" : [ "MEETS_ALL", "MEETS_ANY" ]
        }
      },
      "additionalProperties" : False,
      "required" : [ "Behavior", "Conditions", "Requirement" ]
    },
    "Condition" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ActionCondition" : {
          "description" : "A single action condition.",
          "type" : "object",
          "additionalProperties" : False,
          "properties" : {
            "Action" : {
              "description" : "Logic to apply to the filtering conditions. You can specify that, in order to satisfy the filter, a log must match all conditions or must match at least one condition.",
              "type" : "string",
              "enum" : [ "ALLOW", "BLOCK", "COUNT", "CAPTCHA", "CHALLENGE", "EXCLUDED_AS_COUNT" ]
            }
          },
          "required" : [ "Action" ]
        },
        "LabelNameCondition" : {
          "description" : "A single label name condition.",
          "type" : "object",
          "additionalProperties" : False,
          "properties" : {
            "LabelName" : {
              "description" : "The label name that a log record must contain in order to meet the condition. This must be a fully qualified label name. Fully qualified labels have a prefix, optional namespaces, and label name. The prefix identifies the rule group or web ACL context of the rule that added the label. ",
              "type" : "string"
            }
          },
          "required" : [ "LabelName" ]
        }
      }
    },
    "FieldToMatch" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Method" : {
          "description" : "Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform. ",
          "type" : "object"
        },
        "QueryString" : {
          "type" : "object",
          "description" : "Inspect the query string. This is the part of a URL that appears after a ? character, if any. "
        },
        "SingleHeader" : {
          "description" : "Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer. This setting isn't case sensitive.",
          "type" : "object",
          "additionalProperties" : False,
          "properties" : {
            "Name" : {
              "description" : "The name of the query header to inspect.",
              "type" : "string"
            }
          },
          "required" : [ "Name" ]
        },
        "UriPath" : {
          "type" : "object",
          "description" : "Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg. "
        }
      }
    }
  },
  "properties" : {
    "ResourceArn" : {
      "description" : "The Amazon Resource Name (ARN) of the web ACL that you want to associate with LogDestinationConfigs.",
      "type" : "string"
    },
    "LogDestinationConfigs" : {
      "description" : "The Amazon Resource Names (ARNs) of the logging destinations that you want to associate with the web ACL.",
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "RedactedFields" : {
      "description" : "The parts of the request that you want to keep out of the logs. For example, if you redact the HEADER field, the HEADER field in the firehose will be xxx.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/FieldToMatch"
      }
    },
    "ManagedByFirewallManager" : {
      "description" : "Indicates whether the logging configuration was created by AWS Firewall Manager, as part of an AWS WAF policy configuration. If True, only Firewall Manager can modify or delete the configuration.",
      "type" : "boolean"
    },
    "LoggingFilter" : {
      "description" : "Filtering that specifies which web requests are kept in the logs and which are dropped. You can filter on the rule action and on the web request labels that were applied by matching rules during web ACL evaluation.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DefaultBehavior" : {
          "description" : "Default handling for logs that don't match any of the specified filtering conditions.",
          "type" : "string",
          "enum" : [ "KEEP", "DROP" ]
        },
        "Filters" : {
          "description" : "The filters that you want to apply to the logs.",
          "type" : "array",
          "minItems" : 1,
          "items" : {
            "$ref" : "#/definitions/Filter"
          }
        }
      },
      "required" : [ "DefaultBehavior", "Filters" ]
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "cloudFormationSystemTags" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "taggable" : False
  },
  "required" : [ "ResourceArn", "LogDestinationConfigs" ],
  "createOnlyProperties" : [ "/properties/ResourceArn" ],
  "readOnlyProperties" : [ "/properties/ManagedByFirewallManager" ],
  "primaryIdentifier" : [ "/properties/ResourceArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "wafv2:PutLoggingConfiguration", "wafv2:GetLoggingConfiguration", "firehose:ListDeliveryStreams", "iam:CreateServiceLinkedRole", "iam:DescribeOrganization", "logs:CreateLogDelivery", "s3:PutBucketPolicy", "s3:GetBucketPolicy", "logs:PutResourcePolicy", "logs:DescribeResourcePolicies", "logs:DescribeLogGroups" ]
    },
    "read" : {
      "permissions" : [ "wafv2:GetLoggingConfiguration" ]
    },
    "update" : {
      "permissions" : [ "wafv2:PutLoggingConfiguration", "wafv2:GetLoggingConfiguration", "firehose:ListDeliveryStreams", "iam:CreateServiceLinkedRole", "iam:DescribeOrganization", "logs:CreateLogDelivery", "s3:PutBucketPolicy", "s3:GetBucketPolicy", "logs:PutResourcePolicy", "logs:DescribeResourcePolicies", "logs:DescribeLogGroups" ]
    },
    "delete" : {
      "permissions" : [ "wafv2:DeleteLoggingConfiguration", "wafv2:GetLoggingConfiguration", "logs:DeleteLogDelivery" ]
    },
    "list" : {
      "permissions" : [ "wafv2:ListLoggingConfigurations" ]
    }
  }
}