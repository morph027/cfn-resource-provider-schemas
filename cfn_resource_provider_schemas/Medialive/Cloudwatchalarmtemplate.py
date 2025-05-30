SCHEMA = {
  "typeName" : "AWS::MediaLive::CloudWatchAlarmTemplate",
  "description" : "Definition of AWS::MediaLive::CloudWatchAlarmTemplate Resource Type",
  "definitions" : {
    "CloudWatchAlarmTemplateComparisonOperator" : {
      "type" : "string",
      "description" : "The comparison operator used to compare the specified statistic and the threshold.",
      "enum" : [ "GreaterThanOrEqualToThreshold", "GreaterThanThreshold", "LessThanThreshold", "LessThanOrEqualToThreshold" ]
    },
    "CloudWatchAlarmTemplateStatistic" : {
      "type" : "string",
      "description" : "The statistic to apply to the alarm's metric data.",
      "enum" : [ "SampleCount", "Average", "Sum", "Minimum", "Maximum" ]
    },
    "CloudWatchAlarmTemplateTargetResourceType" : {
      "type" : "string",
      "description" : "The resource type this template should dynamically generate cloudwatch metric alarms for.",
      "enum" : [ "CLOUDFRONT_DISTRIBUTION", "MEDIALIVE_MULTIPLEX", "MEDIALIVE_CHANNEL", "MEDIALIVE_INPUT_DEVICE", "MEDIAPACKAGE_CHANNEL", "MEDIAPACKAGE_ORIGIN_ENDPOINT", "MEDIACONNECT_FLOW", "MEDIATAILOR_PLAYBACK_CONFIGURATION", "S3_BUCKET" ]
    },
    "CloudWatchAlarmTemplateTreatMissingData" : {
      "type" : "string",
      "description" : "Specifies how missing data points are treated when evaluating the alarm's condition.",
      "enum" : [ "notBreaching", "breaching", "ignore", "missing" ]
    },
    "TagMap" : {
      "type" : "object",
      "description" : "Represents the tags associated with a resource.",
      "patternProperties" : {
        ".+" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "pattern" : "^arn:.+:medialive:.+:cloudwatch-alarm-template:.+$",
      "description" : "A cloudwatch alarm template's ARN (Amazon Resource Name)"
    },
    "ComparisonOperator" : {
      "$ref" : "#/definitions/CloudWatchAlarmTemplateComparisonOperator"
    },
    "CreatedAt" : {
      "type" : "string",
      "format" : "date-time"
    },
    "DatapointsToAlarm" : {
      "type" : "number",
      "default" : 0,
      "minimum" : 1,
      "description" : "The number of datapoints within the evaluation period that must be breaching to trigger the alarm."
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 1024,
      "minLength" : 0,
      "description" : "A resource's optional description."
    },
    "EvaluationPeriods" : {
      "type" : "number",
      "default" : 0,
      "minimum" : 1,
      "description" : "The number of periods over which data is compared to the specified threshold."
    },
    "GroupId" : {
      "type" : "string",
      "maxLength" : 11,
      "minLength" : 7,
      "pattern" : "^(aws-)?[0-9]{7}$",
      "description" : "A cloudwatch alarm template group's id. AWS provided template groups have ids that start with `aws-`"
    },
    "GroupIdentifier" : {
      "type" : "string",
      "pattern" : "^[^\\s]+$",
      "description" : "A cloudwatch alarm template group's identifier. Can be either be its id or current name."
    },
    "Id" : {
      "type" : "string",
      "maxLength" : 11,
      "minLength" : 7,
      "pattern" : "^(aws-)?[0-9]{7}$",
      "description" : "A cloudwatch alarm template's id. AWS provided templates have ids that start with `aws-`"
    },
    "Identifier" : {
      "type" : "string"
    },
    "MetricName" : {
      "type" : "string",
      "maxLength" : 64,
      "minLength" : 0,
      "description" : "The name of the metric associated with the alarm. Must be compatible with targetResourceType."
    },
    "ModifiedAt" : {
      "type" : "string",
      "format" : "date-time"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 255,
      "minLength" : 1,
      "pattern" : "^[^\\s]+$",
      "description" : "A resource's name. Names must be unique within the scope of a resource type in a specific region."
    },
    "Period" : {
      "type" : "number",
      "default" : 0,
      "maximum" : 86400,
      "minimum" : 10,
      "description" : "The period, in seconds, over which the specified statistic is applied."
    },
    "Statistic" : {
      "$ref" : "#/definitions/CloudWatchAlarmTemplateStatistic"
    },
    "Tags" : {
      "$ref" : "#/definitions/TagMap"
    },
    "TargetResourceType" : {
      "$ref" : "#/definitions/CloudWatchAlarmTemplateTargetResourceType"
    },
    "Threshold" : {
      "type" : "number",
      "default" : 0,
      "description" : "The threshold value to compare with the specified statistic."
    },
    "TreatMissingData" : {
      "$ref" : "#/definitions/CloudWatchAlarmTemplateTreatMissingData"
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "medialive:CreateTags", "medialive:DeleteTags" ]
  },
  "required" : [ "ComparisonOperator", "EvaluationPeriods", "MetricName", "Name", "Period", "Statistic", "TargetResourceType", "Threshold", "TreatMissingData" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreatedAt", "/properties/Id", "/properties/GroupId", "/properties/Identifier", "/properties/ModifiedAt" ],
  "writeOnlyProperties" : [ "/properties/GroupIdentifier" ],
  "createOnlyProperties" : [ "/properties/Tags" ],
  "primaryIdentifier" : [ "/properties/Identifier" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "medialive:CreateCloudWatchAlarmTemplate", "medialive:GetCloudWatchAlarmTemplate", "medialive:CreateTags" ]
    },
    "read" : {
      "permissions" : [ "medialive:GetCloudWatchAlarmTemplate" ]
    },
    "update" : {
      "permissions" : [ "medialive:UpdateCloudWatchAlarmTemplate", "medialive:GetCloudWatchAlarmTemplate", "medialive:CreateTags", "medialive:DeleteTags" ]
    },
    "delete" : {
      "permissions" : [ "medialive:DeleteCloudWatchAlarmTemplate" ]
    },
    "list" : {
      "permissions" : [ "medialive:ListCloudWatchAlarmTemplates" ]
    }
  },
  "additionalProperties" : False
}