---
sidebar_position: 2
---

# RQL Functions


## Usage

### type Alert

```go
type Alert struct {
        Result *model.Alert `json:"result"`
        Error  string       `json:"error"`
}
```


### type Alerts

```go
type Alerts struct {
        Result []model.Alert `json:"result"`
        Error  string        `json:"error"`
}
```


### type CurrentWeather

```go
type CurrentWeather struct {
        Location struct {
                Name           string  `json:"name"`
                Region         string  `json:"region"`
                Country        string  `json:"country"`
                Lat            float64 `json:"lat"`
                Lon            float64 `json:"lon"`
                TzId           string  `json:"tz_id"`
                LocaltimeEpoch int     `json:"localtime_epoch"`
                Localtime      string  `json:"localtime"`
        } `json:"location"`
        Current struct {
                LastUpdatedEpoch int     `json:"last_updated_epoch"`
                LastUpdated      string  `json:"last_updated"`
                TempC            float64 `json:"temp_c"`
                TempF            float64 `json:"temp_f"`
                IsDay            int     `json:"is_day"`
                Condition        struct {
                        Text string `json:"text"`
                        Icon string `json:"icon"`
                        Code int    `json:"code"`
                } `json:"condition"`
                WindMph    float64 `json:"wind_mph"`
                WindKph    float64 `json:"wind_kph"`
                WindDegree int     `json:"wind_degree"`
                WindDir    string  `json:"wind_dir"`
                PressureMb float64 `json:"pressure_mb"`
                PressureIn float64 `json:"pressure_in"`
                PrecipMm   float64 `json:"precip_mm"`
                PrecipIn   float64 `json:"precip_in"`
                Humidity   int     `json:"humidity"`
                Cloud      int     `json:"cloud"`
                FeelslikeC float64 `json:"feelslike_c"`
                FeelslikeF float64 `json:"feelslike_f"`
                VisKm      float64 `json:"vis_km"`
                VisMiles   float64 `json:"vis_miles"`
                Uv         float64 `json:"uv"`
                GustMph    float64 `json:"gust_mph"`
                GustKph    float64 `json:"gust_kph"`
        } `json:"current"`
}
```


### type CurrentWeatherResponse

```go
type CurrentWeatherResponse struct {
        Result *CurrentWeather
        Error  string
}
```


### type Forecast

```go
type Forecast struct {
        Location struct {
                Name           string  `json:"name"`
                Region         string  `json:"region"`
                Country        string  `json:"country"`
                Lat            float64 `json:"lat"`
                Lon            float64 `json:"lon"`
                TzId           string  `json:"tz_id"`
                LocaltimeEpoch int     `json:"localtime_epoch"`
                Localtime      string  `json:"localtime"`
        } `json:"location"`
        Current struct {
                LastUpdatedEpoch int     `json:"last_updated_epoch"`
                LastUpdated      string  `json:"last_updated"`
                TempC            float64 `json:"temp_c"`
                TempF            float64 `json:"temp_f"`
                IsDay            int     `json:"is_day"`
                Condition        struct {
                        Text string `json:"text"`
                        Icon string `json:"icon"`
                        Code int    `json:"code"`
                } `json:"condition"`
                WindMph    float64 `json:"wind_mph"`
                WindKph    float64 `json:"wind_kph"`
                WindDegree int     `json:"wind_degree"`
                WindDir    string  `json:"wind_dir"`
                PressureMb float64 `json:"pressure_mb"`
                PressureIn float64 `json:"pressure_in"`
                PrecipMm   float64 `json:"precip_mm"`
                PrecipIn   float64 `json:"precip_in"`
                Humidity   int     `json:"humidity"`
                Cloud      int     `json:"cloud"`
                FeelslikeC float64 `json:"feelslike_c"`
                FeelslikeF float64 `json:"feelslike_f"`
                VisKm      float64 `json:"vis_km"`
                VisMiles   float64 `json:"vis_miles"`
                Uv         float64 `json:"uv"`
                GustMph    float64 `json:"gust_mph"`
                GustKph    float64 `json:"gust_kph"`
        } `json:"current"`
        Forecast struct {
                Forecastday []struct {
                        Date      string `json:"date"`
                        DateEpoch int    `json:"date_epoch"`
                        Day       struct {
                                MaxtempC          float64 `json:"maxtemp_c"`
                                MaxtempF          float64 `json:"maxtemp_f"`
                                MintempC          float64 `json:"mintemp_c"`
                                MintempF          float64 `json:"mintemp_f"`
                                AvgtempC          float64 `json:"avgtemp_c"`
                                AvgtempF          float64 `json:"avgtemp_f"`
                                MaxwindMph        float64 `json:"maxwind_mph"`
                                MaxwindKph        float64 `json:"maxwind_kph"`
                                TotalprecipMm     float64 `json:"totalprecip_mm"`
                                TotalprecipIn     float64 `json:"totalprecip_in"`
                                TotalsnowCm       float64 `json:"totalsnow_cm"`
                                AvgvisKm          float64 `json:"avgvis_km"`
                                AvgvisMiles       float64 `json:"avgvis_miles"`
                                Avghumidity       float64 `json:"avghumidity"`
                                DailyWillItRain   int     `json:"daily_will_it_rain"`
                                DailyChanceOfRain int     `json:"daily_chance_of_rain"`
                                DailyWillItSnow   int     `json:"daily_will_it_snow"`
                                DailyChanceOfSnow int     `json:"daily_chance_of_snow"`
                                Condition         struct {
                                        Text string `json:"text"`
                                        Icon string `json:"icon"`
                                        Code int    `json:"code"`
                                } `json:"condition"`
                                Uv float64 `json:"uv"`
                        } `json:"day"`
                        Astro struct {
                                Sunrise          string `json:"sunrise"`
                                Sunset           string `json:"sunset"`
                                Moonrise         string `json:"moonrise"`
                                Moonset          string `json:"moonset"`
                                MoonPhase        string `json:"moon_phase"`
                                MoonIllumination string `json:"moon_illumination"`
                                IsMoonUp         int    `json:"is_moon_up"`
                                IsSunUp          int    `json:"is_sun_up"`
                        } `json:"astro"`
                        Hour []struct {
                                TimeEpoch int     `json:"time_epoch"`
                                Time      string  `json:"time"`
                                TempC     float64 `json:"temp_c"`
                                TempF     float64 `json:"temp_f"`
                                IsDay     int     `json:"is_day"`
                                Condition struct {
                                        Text string `json:"text"`
                                        Icon string `json:"icon"`
                                        Code int    `json:"code"`
                                } `json:"condition"`
                                WindMph      float64 `json:"wind_mph"`
                                WindKph      float64 `json:"wind_kph"`
                                WindDegree   int     `json:"wind_degree"`
                                WindDir      string  `json:"wind_dir"`
                                PressureMb   float64 `json:"pressure_mb"`
                                PressureIn   float64 `json:"pressure_in"`
                                PrecipMm     float64 `json:"precip_mm"`
                                PrecipIn     float64 `json:"precip_in"`
                                Humidity     int     `json:"humidity"`
                                Cloud        int     `json:"cloud"`
                                FeelslikeC   float64 `json:"feelslike_c"`
                                FeelslikeF   float64 `json:"feelslike_f"`
                                WindchillC   float64 `json:"windchill_c"`
                                WindchillF   float64 `json:"windchill_f"`
                                HeatindexC   float64 `json:"heatindex_c"`
                                HeatindexF   float64 `json:"heatindex_f"`
                                DewpointC    float64 `json:"dewpoint_c"`
                                DewpointF    float64 `json:"dewpoint_f"`
                                WillItRain   int     `json:"will_it_rain"`
                                ChanceOfRain int     `json:"chance_of_rain"`
                                WillItSnow   int     `json:"will_it_snow"`
                                ChanceOfSnow int     `json:"chance_of_snow"`
                                VisKm        float64 `json:"vis_km"`
                                VisMiles     float64 `json:"vis_miles"`
                                GustMph      float64 `json:"gust_mph"`
                                GustKph      float64 `json:"gust_kph"`
                                Uv           float64 `json:"uv"`
                        } `json:"hour"`
                } `json:"forecastday"`
        } `json:"forecast"`
        Alerts struct {
                Alert []struct {
                        Headline    string    `json:"headline"`
                        Msgtype     string    `json:"msgtype"`
                        Severity    string    `json:"severity"`
                        Urgency     string    `json:"urgency"`
                        Areas       string    `json:"areas"`
                        Category    string    `json:"category"`
                        Certainty   string    `json:"certainty"`
                        Event       string    `json:"event"`
                        Note        string    `json:"note"`
                        Effective   time.Time `json:"effective"`
                        Expires     time.Time `json:"expires"`
                        Desc        string    `json:"desc"`
                        Instruction string    `json:"instruction"`
                } `json:"alert"`
        } `json:"alerts"`
}
```


### type ForecastResponse

```go
type ForecastResponse struct {
        Result *Forecast
        Error  string
}
```


### type HTTPBody

```go
type HTTPBody struct {
        Url          string `json:"url"`
        Method       string
        ResponseType string `json:"response_type"` //json, string
        Headers      map[string]string
}
```


### type HTTPGet

```go
type HTTPGet struct {
        Result any
        Error  string
}
```


### type Histories

```go
type Histories struct {
        Result []model.PointHistory `json:"result"`
        Error  string               `json:"error"`
}
```


### type Host

```go
type Host struct {
        Result *model.Host `json:"result"`
        Error  string      `json:"error"`
}
```


### type Hosts

```go
type Hosts struct {
        Result []model.Host `json:"result"`
        Error  string       `json:"error"`
}
```


### type IsPublicHoliday

```go
type IsPublicHoliday struct {
        IsPublicHoliday bool
        Name            string
        Locations       []string `json:"locations"`
}
```


### type IsPublicHolidayResponse

```go
type IsPublicHolidayResponse struct {
        Result *IsPublicHoliday
        Error  string
}
```


### type Mail

```go
type Mail struct {
        To            []string
        Cc            []string
        Bcc           []string
        Subject       string
        Message       string
        SenderAddress string
        Password      string
}
```


### type PDFResponse

```go
type PDFResponse struct {
        Result []PingResult
        Error  string
}
```


### type PdfBody

```go
type PdfBody struct {
        Text string `json:"text"`
}
```


### type PingResponse

```go
type PingResponse struct {
        Result any
        Error  string
}
```


### type PingResult

```go
type PingResult struct {
        Ip string `json:"ip"`
        Ok bool   `json:"ok"`
}
```


### type Point

```go
type Point struct {
        Result *model.Point `json:"result"`
        Error  string       `json:"error"`
}
```


### type Points

```go
type Points struct {
        Result []model.Point `json:"result"`
        Error  string        `json:"error"`
}
```


### type PublicHolidays

```go
type PublicHolidays struct {
        Date        string   `json:"date"`
        LocalName   string   `json:"localName"`
        Name        string   `json:"name"`
        CountryCode string   `json:"countryCode"`
        Fixed       bool     `json:"fixed"`
        Global      bool     `json:"global"`
        Counties    []string `json:"counties"`
        LaunchYear  int      `json:"launchYear"`
        Types       []string `json:"types"`
}
```


### type PublicHolidaysResponse

```go
type PublicHolidaysResponse struct {
        Result []PublicHolidays
        Error  string
}
```


### type RQL

```go
type RQL struct {
        Return    interface{}      `json:"return"`
        Err       string           `json:"err"`
        TimeTaken string           `json:"time_taken"`
        Storage   storage.IStorage `json:"-"`
}
```


### func (*RQL) AddAlert

```go
func (inst *RQL) AddAlert(hostIDName string, body any) *Alert
```

### func (*RQL) Date

```go
func (inst *RQL) Date() string
```
Date returns date formatted as `2006.01.02`

### func (*RQL) Day

```go
func (inst *RQL) Day() string
```
Day returns current day

### func (*RQL) GetAlerts

```go
func (inst *RQL) GetAlerts(hostIDName string) *Alerts
```

### func (*RQL) GetCurrentWeather

```go
func (inst *RQL) GetCurrentWeather(apiKey, city string) *CurrentWeatherResponse
```

### func (*RQL) GetForecast

```go
func (inst *RQL) GetForecast(apiKey, city string, days int) *ForecastResponse
```

### func (*RQL) GetHosts

```go
func (inst *RQL) GetHosts() *Hosts
```

### func (*RQL) GetPoint

```go
func (inst *RQL) GetPoint(hostIDName, uuid string) *Point
```

### func (*RQL) GetPointHistories

```go
func (inst *RQL) GetPointHistories(hostIDName string, pointUUIDs []string) *Histories
```
GetPointHistories get ROS Histories

### func (*RQL) GetPoints

```go
func (inst *RQL) GetPoints(hostIDName string) *Points
```

### func (*RQL) GetPublicHolidays

```go
func (inst *RQL) GetPublicHolidays(year, countryCode string) *PublicHolidaysResponse
```

### func (*RQL) GetPublicHolidaysByState

```go
func (inst *RQL) GetPublicHolidaysByState(year, countryCode, state string) *PublicHolidaysResponse
```

### func (*RQL) GetScripts

```go
func (inst *RQL) GetScripts() *ScriptsResponse
```

### func (*RQL) GetVariable

```go
func (inst *RQL) GetVariable(uuidName string) *VarResponse
```

### func (*RQL) GetVariables

```go
func (inst *RQL) GetVariables() *VarsResponse
```

### func (*RQL) HTTPGet

```go
func (inst *RQL) HTTPGet(body *HTTPBody) *HTTPGet
```

### func (*RQL) IsPublicHoliday

```go
func (inst *RQL) IsPublicHoliday(year, countryCode, date string) *IsPublicHolidayResponse
```

### func (*RQL) LimitToRange

```go
func (inst *RQL) LimitToRange(value float64, range1 float64, range2 float64) float64
```
LimitToRange returns the input value clamped within the specified range

### func (*RQL) PDF

```go
func (inst *RQL) PDF(pdfBody *PdfBody) *PingResponse
```

### func (*RQL) Ping

```go
func (inst *RQL) Ping(ipList []string) *PingResponse
```
Ping ping an list of IP address eg: ["192.168.15.1", "192.168.15.2"] will return
[]PingResult

### func (*RQL) Print

```go
func (inst *RQL) Print(x interface{})
```
Print console log a value

### func (*RQL) RandFloat

```go
func (inst *RQL) RandFloat(range1, range2 float64) float64
```
RandFloat returns a random float64 within the specified range.

### func (*RQL) RandInt

```go
func (inst *RQL) RandInt(range1, range2 int) int
```
RandInt returns a random int within the specified range.

### func (*RQL) RoundTo

```go
func (inst *RQL) RoundTo(value float64, decimals uint32) float64
```
RoundTo returns the input value rounded to the specified number of decimal
places.

### func (*RQL) Scale

```go
func (inst *RQL) Scale(value, inMin, inMax, outMin, outMax float64) float64
```
Scale returns the (float64) input value (between inputMin and inputMax) scaled
to a value between outputMin and outputMax

### func (*RQL) SendEmail

```go
func (inst *RQL) SendEmail(body *Mail) error
```
SendEmail example let body = {

    to: ["a@nube-io.com"],
    subject: "test",
    message: "testing",
    senderAddress: "aa@nube-io.com",
    password: "abc",

};

RQL.SendEmail(body);

### func (*RQL) Slack

```go
func (inst *RQL) Slack(body any)
```

### func (*RQL) Sleep

```go
func (inst *RQL) Sleep(duration int)
```
Sleep will delay the program for the `duration` passed in (duration is units
seconds)

### func (*RQL) Tags

```go
func (inst *RQL) Tags(tag ...string)
```

### func (*RQL) Time

```go
func (inst *RQL) Time() string
```
Time returns time formatted as `15:04:05`

### func (*RQL) TimeDate

```go
func (inst *RQL) TimeDate() string
```
TimeDate returns time/date formatted as `2006.01.02 15:04:05`

### func (*RQL) TimeDateDay

```go
func (inst *RQL) TimeDateDay() string
```
TimeDateDay returns time/date formatted as `2006-01-02 15:04:05 Monday`

### func (*RQL) TimeUTC

```go
func (inst *RQL) TimeUTC() time.Time
```
TimeUTC returns time in UTC

### func (*RQL) TimeWithMS

```go
func (inst *RQL) TimeWithMS() string
```
TimeWithMS returns time formatted as `15:04:05.000`

### func (*RQL) ToString

```go
func (inst *RQL) ToString(x interface{}) string
```
ToString convert any value to a string

### func (*RQL) VarParseArray

```go
func (inst *RQL) VarParseArray(uuidName string) interface{}
```
VarParseArray [1, 2, "hello"]

let data = JSON.parse(RQL.VarParseArray("array")); RQL.Return = data;

### func (*RQL) VarParseNumber

```go
func (inst *RQL) VarParseNumber(uuidName string) float64
```

### func (*RQL) VarParseObject

```go
func (inst *RQL) VarParseObject(uuidName string) interface{}
```
VarParseObject `{"sp":22.3,"db":99.9}`

let data = RQL.VarParseObject("obj"); let sp = JSON.parse(data); RQL.Return =
sp["sp"];

### func (*RQL) VarParseString

```go
func (inst *RQL) VarParseString(uuidName string) string
```

### func (*RQL) WeatherByTownAU

```go
func (inst *RQL) WeatherByTownAU(town, state string) *WeatherByTownAUResp
```

### func (*RQL) WritePointValue

```go
func (inst *RQL) WritePointValue(hostIDName, uuid string, value *model.Priority) *Point
```

### func (*RQL) WritePointValuePriority

```go
func (inst *RQL) WritePointValuePriority(hostIDName, uuid string, pri int, value float64) *Point
```

### func (*RQL) Year

```go
func (inst *RQL) Year() string
```
Year returns current year

### type ScriptsResponse

```go
type ScriptsResponse struct {
        Result []storage.RQLRule
        Error  string
}
```


### type VarResponse

```go
type VarResponse struct {
        Result *storage.RQLVariables
        Error  string
}
```


### type VarsResponse

```go
type VarsResponse struct {
        Result []storage.RQLVariables
        Error  string
}
```


### type WeatherByTownAUResp

```go
type WeatherByTownAUResp struct {
        Result *bom.Observations
        Error  string
}
```
