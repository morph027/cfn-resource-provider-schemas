SCHEMA = {
  "typeName" : "AWS::Lightsail::Alarm",
  "description" : "Resource Type definition for AWS::Lightsail::Alarm",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-lightsail.git",
  "properties" : {
    "AlarmName" : {
      "description" : "The name for the alarm. Specify the name of an existing alarm to update, and overwrite the previous configuration of the alarm.",
      "type" : "string",
      "pattern" : "\\w[\\w\\-]*\\w"
    },
    "MonitoredResourceName" : {
      "description" : "The name of the Lightsail resource that the alarm monitors.",
      "type" : "string"
    },
    "MetricName" : {
      "description" : "The name of the metric to associate with the alarm.",
      "type" : "string"
    },
    "ComparisonOperator" : {
      "description" : "The arithmetic operation to use when comparing the specified statistic to the threshold. The specified statistic value is used as the first operand.",
      "type" : "string"
    },
    "ContactProtocols" : {
      "description" : "The contact protocols to use for the alarm, such as Email, SMS (text messaging), or both.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "AlarmArn" : {
      "type" : "string"
    },
    "DatapointsToAlarm" : {
      "description" : "The number of data points that must be not within the specified threshold to trigger the alarm. If you are setting an \"M out of N\" alarm, this value (datapointsToAlarm) is the M.",
      "type" : "integer"
    },
    "EvaluationPeriods" : {
      "description" : "The number of most recent periods over which data is compared to the specified threshold. If you are setting an \"M out of N\" alarm, this value (evaluationPeriods) is the N.",
      "type" : "integer"
    },
    "NotificationEnabled" : {
      "description" : "Indicates whether the alarm is enabled. Notifications are enabled by default if you don't specify this parameter.",
      "type" : "boolean"
    },
    "NotificationTriggers" : {
      "description" : "The alarm states that trigger a notification.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "Threshold" : {
      "description" : "The value against which the specified statistic is compared.",
      "type" : "number"
    },
    "TreatMissingData" : {
      "description" : "Sets how this alarm will handle missing data points.",
      "type" : "string"
    },
    "State" : {
      "description" : "The current state of the alarm.",
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "required" : [ "AlarmName", "MonitoredResourceName", "MetricName", "ComparisonOperator", "EvaluationPeriods", "Threshold" ],
  "readOnlyProperties" : [ "/properties/AlarmArn", "/properties/State" ],
  "taggable" : True,
  "primaryIdentifier" : [ "/properties/AlarmName" ],
  "createOnlyProperties" : [ "/properties/AlarmName", "/properties/MonitoredResourceName", "/properties/MetricName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "lightsail:PutAlarm", "lightsail:GetAlarms" ]
    },
    "read" : {
      "permissions" : [ "lightsail:GetAlarms" ]
    },
    "update" : {
      "permissions" : [ "lightsail:PutAlarm", "lightsail:GetAlarms" ]
    },
    "delete" : {
      "permissions" : [ "lightsail:DeleteAlarm", "lightsail:GetAlarms" ]
    },
    "list" : {
      "permissions" : [ "lightsail:GetAlarms" ]
    }
  }
}