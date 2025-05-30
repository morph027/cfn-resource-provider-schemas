SCHEMA = {
  "typeName" : "AWS::CloudTrail::Dashboard",
  "description" : "The Amazon CloudTrail dashboard resource allows customers to manage managed dashboards and create custom dashboards. You can manually refresh custom and managed dashboards. For custom dashboards, you can also set up an automatic refresh schedule and modify dashboard widgets.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-cloudtrail.git",
  "definitions" : {
    "RefreshSchedule" : {
      "description" : "Configures the automatic refresh schedule for the dashboard. Includes the frequency unit (DAYS or HOURS) and value, as well as the status (ENABLED or DISABLED) of the refresh schedule.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Frequency" : {
          "type" : "object",
          "additionalProperties" : False,
          "properties" : {
            "Unit" : {
              "description" : "The frequency unit. Supported values are HOURS and DAYS.",
              "type" : "string",
              "enum" : [ "HOURS", "DAYS" ]
            },
            "Value" : {
              "description" : "The frequency value.",
              "type" : "integer"
            }
          },
          "required" : [ "Unit", "Value" ]
        },
        "TimeOfDay" : {
          "type" : "string",
          "description" : "StartTime of the automatic schedule refresh.",
          "pattern" : "^[0-9]{2}:[0-9]{2}"
        },
        "Status" : {
          "type" : "string",
          "description" : "The status of the schedule. Supported values are ENABLED and DISABLED.",
          "enum" : [ "ENABLED", "DISABLED" ]
        }
      },
      "required" : [ ]
    },
    "QueryParameter" : {
      "type" : "string",
      "description" : "The value of the QueryParameter. Possible values: $StartTime$, $EndTime$, $Period$.",
      "minLength" : 1,
      "maxLength" : 1024,
      "pattern" : ".*"
    },
    "Widget" : {
      "description" : "The dashboard widget",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "QueryStatement" : {
          "description" : "The SQL query statement on one or more event data stores.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 10000,
          "pattern" : "(?s).*"
        },
        "QueryParameters" : {
          "description" : "The placeholder keys in the QueryStatement. For example: $StartTime$, $EndTime$, $Period$.",
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/QueryParameter"
          },
          "minItems" : 1,
          "maxItems" : 10,
          "uniqueItems" : False,
          "insertionOrder" : True
        },
        "ViewProperties" : {
          "description" : "The view properties of the widget.",
          "type" : "object",
          "additionalProperties" : False,
          "patternProperties" : {
            "^[a-zA-Z0-9._-]{3,128}$" : {
              "type" : "string",
              "minLength" : 1,
              "maxLength" : 128,
              "pattern" : "^[a-zA-Z0-9._\\- ]+$"
            }
          }
        }
      },
      "required" : [ "QueryStatement" ]
    },
    "Tag" : {
      "description" : "An arbitrary set of tags (key-value pairs) for this dashboard.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "description" : "The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string"
        },
        "Value" : {
          "description" : "The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    },
    "Timestamp" : {
      "type" : "string"
    }
  },
  "properties" : {
    "Widgets" : {
      "description" : "List of widgets on the dashboard",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Widget"
      },
      "uniqueItems" : True,
      "insertionOrder" : True
    },
    "CreatedTimestamp" : {
      "description" : "The timestamp of the dashboard creation.",
      "$ref" : "#/definitions/Timestamp"
    },
    "DashboardArn" : {
      "description" : "The ARN of the dashboard.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9._/\\-:]+$"
    },
    "RefreshSchedule" : {
      "description" : "Configures the automatic refresh schedule for the dashboard. Includes the frequency unit (DAYS or HOURS) and value, as well as the status (ENABLED or DISABLED) of the refresh schedule.",
      "$ref" : "#/definitions/RefreshSchedule"
    },
    "Name" : {
      "description" : "The name of the dashboard.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9_\\-]+$"
    },
    "Status" : {
      "description" : "The status of the dashboard. Values are CREATING, CREATED, UPDATING, UPDATED and DELETING.",
      "type" : "string",
      "enum" : [ "CREATING", "CREATED", "UPDATING", "UPDATED", "DELETING" ]
    },
    "TerminationProtectionEnabled" : {
      "description" : "Indicates whether the dashboard is protected from termination.",
      "type" : "boolean"
    },
    "Type" : {
      "description" : "The type of the dashboard. Values are CUSTOM and MANAGED.",
      "type" : "string",
      "enum" : [ "MANAGED", "CUSTOM" ]
    },
    "UpdatedTimestamp" : {
      "description" : "The timestamp showing when the dashboard was updated, if applicable. UpdatedTimestamp is always either the same or newer than the time shown in CreatedTimestamp.",
      "$ref" : "#/definitions/Timestamp"
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "required" : [ ],
  "readOnlyProperties" : [ "/properties/DashboardArn", "/properties/CreatedTimestamp", "/properties/UpdatedTimestamp", "/properties/Status", "/properties/Type" ],
  "primaryIdentifier" : [ "/properties/DashboardArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "CloudTrail:CreateDashboard", "CloudTrail:AddTags", "CloudTrail:StartQuery", "CloudTrail:StartDashboardRefresh" ]
    },
    "read" : {
      "permissions" : [ "CloudTrail:GetDashboard", "CloudTrail:ListDashboards", "CloudTrail:ListTags" ]
    },
    "update" : {
      "permissions" : [ "CloudTrail:UpdateDashboard", "CloudTrail:AddTags", "CloudTrail:RemoveTags", "CloudTrail:StartQuery", "CloudTrail:StartDashboardRefresh" ]
    },
    "delete" : {
      "permissions" : [ "CloudTrail:DeleteDashboard", "CloudTrail:UpdateDashboard" ]
    },
    "list" : {
      "permissions" : [ "CloudTrail:ListDashboards", "CloudTrail:GetDashboard", "CloudTrail:ListTags" ]
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "CloudTrail:AddTags", "CloudTrail:RemoveTags", "CloudTrail:ListTags" ]
  }
}