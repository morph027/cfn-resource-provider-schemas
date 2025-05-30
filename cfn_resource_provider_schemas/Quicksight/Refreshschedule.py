SCHEMA = {
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-quicksight",
  "typeName" : "AWS::QuickSight::RefreshSchedule",
  "description" : "Definition of the AWS::QuickSight::RefreshSchedule Resource Type.",
  "definitions" : {
    "RefreshScheduleMap" : {
      "type" : "object",
      "properties" : {
        "ScheduleId" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "description" : "<p>An unique identifier for the refresh schedule.</p>"
        },
        "ScheduleFrequency" : {
          "type" : "object",
          "description" : "<p>Information about the schedule frequency.</p>",
          "properties" : {
            "Interval" : {
              "type" : "string",
              "enum" : [ "MINUTE15", "MINUTE30", "HOURLY", "DAILY", "WEEKLY", "MONTHLY" ]
            },
            "RefreshOnDay" : {
              "type" : "object",
              "description" : "<p>The day scheduled for refresh.</p>",
              "properties" : {
                "DayOfWeek" : {
                  "type" : "string",
                  "enum" : [ "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY" ]
                },
                "DayOfMonth" : {
                  "type" : "string",
                  "maxLength" : 128,
                  "minLength" : 1,
                  "description" : "<p>The Day Of Month for scheduled refresh.</p>"
                }
              },
              "additionalProperties" : False,
              "required" : [ ]
            },
            "TimeZone" : {
              "type" : "string",
              "maxLength" : 128,
              "minLength" : 1,
              "description" : "<p>The timezone for scheduled refresh.</p>"
            },
            "TimeOfTheDay" : {
              "type" : "string",
              "maxLength" : 128,
              "minLength" : 1,
              "description" : "<p>The time of the day for scheduled refresh.</p>"
            }
          },
          "additionalProperties" : False,
          "required" : [ ]
        },
        "StartAfterDateTime" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "description" : "<p>The date time after which refresh is to be scheduled</p>"
        },
        "RefreshType" : {
          "type" : "string",
          "enum" : [ "FULL_REFRESH", "INCREMENTAL_REFRESH" ]
        }
      },
      "additionalProperties" : False,
      "required" : [ ]
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "description" : "<p>The Amazon Resource Name (ARN) of the data source.</p>"
    },
    "AwsAccountId" : {
      "type" : "string",
      "maxLength" : 12,
      "minLength" : 12,
      "pattern" : "^[0-9]{12}$"
    },
    "DataSetId" : {
      "type" : "string"
    },
    "Schedule" : {
      "$ref" : "#/definitions/RefreshScheduleMap"
    }
  },
  "additionalProperties" : False,
  "required" : [ ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/AwsAccountId", "/properties/DataSetId", "/properties/Schedule/ScheduleId" ],
  "primaryIdentifier" : [ "/properties/AwsAccountId", "/properties/DataSetId", "/properties/Schedule/ScheduleId" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "quicksight:CreateRefreshSchedule", "quicksight:DescribeRefreshSchedule" ]
    },
    "update" : {
      "permissions" : [ "quicksight:UpdateRefreshSchedule", "quicksight:DescribeRefreshSchedule" ]
    },
    "delete" : {
      "permissions" : [ "quicksight:DeleteRefreshSchedule", "quicksight:DescribeRefreshSchedule" ]
    },
    "list" : {
      "permissions" : [ "quicksight:ListRefreshSchedules" ],
      "handlerSchema" : {
        "properties" : {
          "AwsAccountId" : {
            "$ref" : "resource-schema.json#/properties/AwsAccountId"
          },
          "DataSetId" : {
            "$ref" : "resource-schema.json#/properties/DataSetId"
          }
        },
        "required" : [ "AwsAccountId", "DataSetId" ]
      }
    },
    "read" : {
      "permissions" : [ "quicksight:DescribeRefreshSchedule" ]
    }
  }
}