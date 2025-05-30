SCHEMA = {
  "typeName" : "AWS::SSM::MaintenanceWindow",
  "description" : "Resource Type definition for AWS::SSM::MaintenanceWindow",
  "additionalProperties" : False,
  "properties" : {
    "StartDate" : {
      "type" : "string"
    },
    "Description" : {
      "type" : "string"
    },
    "AllowUnassociatedTargets" : {
      "type" : "boolean"
    },
    "Cutoff" : {
      "type" : "integer"
    },
    "Schedule" : {
      "type" : "string"
    },
    "Duration" : {
      "type" : "integer"
    },
    "ScheduleOffset" : {
      "type" : "integer"
    },
    "Id" : {
      "type" : "string"
    },
    "EndDate" : {
      "type" : "string"
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Name" : {
      "type" : "string"
    },
    "ScheduleTimezone" : {
      "type" : "string"
    }
  },
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
  "required" : [ "AllowUnassociatedTargets", "Cutoff", "Schedule", "Duration", "Name" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}