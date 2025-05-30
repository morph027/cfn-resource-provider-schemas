SCHEMA = {
  "typeName" : "AWS::IoT::ScheduledAudit",
  "description" : "Scheduled audits can be used to specify the checks you want to perform during an audit and how often the audit should be run.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-iot.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The tag's key.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The tag's value.",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "required" : [ "Value", "Key" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "ScheduledAuditName" : {
      "description" : "The name you want to give to the scheduled audit.",
      "type" : "string",
      "pattern" : "[a-zA-Z0-9:_-]+",
      "minLength" : 1,
      "maxLength" : 128
    },
    "Frequency" : {
      "description" : "How often the scheduled audit takes place. Can be one of DAILY, WEEKLY, BIWEEKLY, or MONTHLY.",
      "type" : "string",
      "enum" : [ "DAILY", "WEEKLY", "BIWEEKLY", "MONTHLY" ]
    },
    "DayOfMonth" : {
      "description" : "The day of the month on which the scheduled audit takes place. Can be 1 through 31 or LAST. This field is required if the frequency parameter is set to MONTHLY.",
      "type" : "string",
      "pattern" : "^([1-9]|[12][0-9]|3[01])$|^LAST$|^UNSET_VALUE$"
    },
    "DayOfWeek" : {
      "description" : "The day of the week on which the scheduled audit takes place. Can be one of SUN, MON, TUE,WED, THU, FRI, or SAT. This field is required if the frequency parameter is set to WEEKLY or BIWEEKLY.",
      "type" : "string",
      "enum" : [ "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT", "UNSET_VALUE" ]
    },
    "TargetCheckNames" : {
      "description" : "Which checks are performed during the scheduled audit. Checks must be enabled for your account.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "ScheduledAuditArn" : {
      "description" : "The ARN (Amazon resource name) of the scheduled audit.",
      "type" : "string",
      "minLength" : 20,
      "maxLength" : 2048
    },
    "Tags" : {
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "description" : "An array of key-value pairs to apply to this resource.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/ScheduledAuditName" ],
  "required" : [ "Frequency", "TargetCheckNames" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iot:TagResource", "iot:UntagResource", "iot:ListTagsForResource" ]
  },
  "createOnlyProperties" : [ "/properties/ScheduledAuditName" ],
  "readOnlyProperties" : [ "/properties/ScheduledAuditArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iot:CreateScheduledAudit", "iot:DescribeScheduledAudit", "iot:TagResource" ]
    },
    "read" : {
      "permissions" : [ "iot:DescribeScheduledAudit", "iot:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iot:UpdateScheduledAudit", "iot:ListTagsForResource", "iot:UntagResource", "iot:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "iot:DescribeScheduledAudit", "iot:DeleteScheduledAudit" ]
    },
    "list" : {
      "permissions" : [ "iot:ListScheduledAudits" ]
    }
  }
}