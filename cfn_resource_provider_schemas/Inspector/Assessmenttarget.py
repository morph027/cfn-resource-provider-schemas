SCHEMA = {
  "typeName" : "AWS::Inspector::AssessmentTarget",
  "description" : "Resource Type definition for AWS::Inspector::AssessmentTarget",
  "additionalProperties" : False,
  "properties" : {
    "Arn" : {
      "type" : "string"
    },
    "AssessmentTargetName" : {
      "type" : "string"
    },
    "ResourceGroupArn" : {
      "type" : "string"
    }
  },
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/AssessmentTargetName" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "taggable" : False,
  "handlers" : {
    "create" : {
      "permissions" : [ "inspector:CreateAssessmentTarget", "inspector:ListAssessmentTargets", "inspector:DescribeAssessmentTargets" ]
    },
    "update" : {
      "permissions" : [ "inspector:DescribeAssessmentTargets", "inspector:UpdateAssessmentTarget" ]
    },
    "read" : {
      "permissions" : [ "inspector:DescribeAssessmentTargets" ]
    },
    "delete" : {
      "permissions" : [ "inspector:DeleteAssessmentTarget" ]
    },
    "list" : {
      "permissions" : [ "inspector:ListAssessmentTargets" ]
    }
  }
}